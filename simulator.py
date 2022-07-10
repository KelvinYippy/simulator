from abc import abstractmethod
from bs4 import BeautifulSoup

import requests
from game import Game
from lineup import Lineup
from stadium import Stadium
from constants import sofifa_dictionary

class Simulator():

    def __init__(self, home_name = "", away_name = "") -> None:
        self.home_name: str = home_name
        self.home_lineup: list[str] = []
        self.home_corner_takers: list[str] = []
        self.home_free_kick_takers: list[str] = []
        self.home_penalty_taker: str = ""
        self.away_name: str = away_name
        self.away_lineup: list[str] = []
        self.away_corner_takers: list[str] = []
        self.away_free_kick_takers: list[str] = []
        self.away_penalty_taker: str = ""
        self.stadium_name: str = ""
    
    @abstractmethod
    def get_simulator_info(self):
        pass

    def run_simulator(self):
        self.get_simulator_info()
        home_team = Lineup(self.home_name, self.home_lineup, self.home_corner_takers, self.home_free_kick_takers, self.home_penalty_taker)
        away_team = Lineup(self.away_name, self.away_lineup, self.away_corner_takers, self.away_free_kick_takers, self.away_penalty_taker)
        venue = Stadium(self.stadium_name, 10)
        match = Game(home_team, away_team, False, venue)
        print(match)

class FileSimulator(Simulator):

    def __init__(self, file) -> None:
        super().__init__()
        self._file = file

    def _scan_lineup(self) -> list[str]:
        """Scan lineup from text file and return as list of strings."""
        arr = []
        with open(self._file, 'r') as f:
            file_lines = f.readlines()
            for line in file_lines:
                arr.append(line.rstrip())
        f.close()
        return arr

    def get_simulator_info(self):
        lineups = self._scan_lineup()
        home, away = lineups[0:25], lineups[26:51]
        self.home_name = home[0]
        self.away_name = away[0]
        self.home_lineup = home[3:14]
        self.away_lineup = away[3:14]
        self.home_corner_takers = home[16:18]
        self.away_corner_takers = away[16:18]
        self.home_free_kick_takers = home[20:22]
        self.away_free_kick_takers = away[20:22]
        self.home_penalty_taker = home[24]
        self.away_penalty_taker = away[24]
        self.stadium_name = lineups[53]

class SoFIFASimulator(Simulator):

    def __init__(self, home_name, away_name) -> None:
        super().__init__(home_name, away_name)

    def scrape_team(self, team):
        fetch_html = requests.get(sofifa_dictionary[team]).text
        soup = BeautifulSoup(fetch_html, "html.parser")
        info = soup.find("div", class_="bp3-card player").find("div", class_="card")
        players = soup.find("tbody")
        return {
            "info": info,
            "players": players
        }

    def get_starters(self, players):
        starters = players.find_all("tr", class_="starting")
        names = [starter.find("td", class_="col-name").find("a", role="tooltip").get_text() for starter in starters]
        positions = [starter.find_all("td", class_="col-name")[1].find("span").get_text() for starter in starters]
        ratings = [starter.find("td", class_="col col-oa").get_text() for starter in starters]
        arr = []
        for i in range(11):
            arr.append(f"{positions[i]} {names[i]} {ratings[i]}")
        return arr

    def info_helper(self, info):
        return info.find("ul", class_="pl").find_all("li")

    def get_corner_takers(self, info):
        array = []
        corner_takers = self.info_helper(info)[-2:]
        for corner_taker in corner_takers:
            array.append(corner_taker.find("a").get_text())
        return array

    def get_free_kick_takers(self, info):
        array = []
        free_kick_takers = self.info_helper(info)[9:11]
        for free_kick_taker in free_kick_takers:
            array.append(free_kick_taker.find("a").get_text())
        return array

    def get_penalty_kick_taker(self, info):
        penalty_kick_taker = self.info_helper(info)[-3]
        return penalty_kick_taker.find("a").get_text()

    def get_stadium(self, info):
        stadium_name = self.info_helper(info)[0]
        stadium_name.find("label").decompose()
        return stadium_name.get_text()

    def get_simulator_info(self):
        home_team = self.scrape_team(self.home_name)
        self.home_lineup = self.get_starters(home_team["players"])
        self.home_corner_takers = self.get_corner_takers(home_team["info"])
        self.home_free_kick_takers = self.get_free_kick_takers(home_team["info"])
        self.home_penalty_taker = self.get_penalty_kick_taker(home_team["info"])
        away_team = self.scrape_team(self.away_name)
        self.away_lineup = self.get_starters(away_team["players"])
        self.away_corner_takers = self.get_corner_takers(away_team["info"])
        self.away_free_kick_takers = self.get_free_kick_takers(away_team["info"])
        self.away_penalty_taker = self.get_penalty_kick_taker(away_team["info"])
        self.stadium_name = self.get_stadium(home_team["info"])

if __name__ == "__main__":
    SoFIFASimulator("Manchester United", "Arsenal").run_simulator()