from abc import abstractmethod
from bs4 import BeautifulSoup, Tag
from utils import fetch
from match import Match
from lineup import Lineup
from stadium import Stadium
from player import Player
from enum import Enum

class TeamType(Enum):
    HOME = 1,
    AWAY = 2

class Simulator():

    def __init__(self, home_name = "", away_name = "") -> None:
        self.home_name: str = home_name
        self.home_lineup: list[Player] = []
        self.home_lineup_map: dict[str, Player] = {}
        self.home_corner_takers: list[Player] = []
        self.home_free_kick_takers: list[Player] = []
        self.home_penalty_taker: Player = ""
        self.away_name: str = away_name
        self.away_lineup: list[Player] = []
        self.away_lineup_map: dict[str, Player] = {}
        self.away_corner_takers: list[Player] = []
        self.away_free_kick_takers: list[Player] = []
        self.away_penalty_taker: Player = ""
        self.stadium_name: str = ""
        self.home_away_map = {
            TeamType.HOME: self.home_lineup_map,
            TeamType.AWAY: self.away_lineup_map
        }
    
    @abstractmethod
    def get_simulator_info(self):
        pass

    def run_simulator(self):
        """Run the actual simulator to print out the result of the match."""
        self.get_simulator_info()
        home_team = Lineup(self.home_name, self.home_lineup, self.home_corner_takers, self.home_free_kick_takers, self.home_penalty_taker, False)
        away_team = Lineup(self.away_name, self.away_lineup, self.away_corner_takers, self.away_free_kick_takers, self.away_penalty_taker, False)
        venue = Stadium(self.stadium_name, 10)
        match = Match(home_team, away_team, False, venue)
        print(match)
        return match 

class FileSimulator(Simulator):

    def __init__(self, file) -> None:
        super().__init__()
        self._file = file

    def _scan_lineup(self) -> list[str]:
        """Scan lineup from text file and return as list of strings."""
        arr = []
        with open(self._file, 'r') as f:
            file_lines = f.readlines()
            arr = [line.rstrip() for line in file_lines]
        f.close()
        return arr

    def get_simulator_info(self):
        """Parse the scanned lineup to get information about lineups, match location, and set-piece takers."""
        def create_lineup(lineup: list[str]):
            players = []
            for player in lineup:
                player_attributes = player.split()
                position = player_attributes.pop(0)
                rating = player_attributes.pop()
                name = " ".join(player_attributes)
                formatted_player = Player(name, position, rating)
                players.append(formatted_player)
            return players
        lineups = self._scan_lineup()
        home, away = lineups[0:25], lineups[26:51]
        self.home_name = home[0]
        self.away_name = away[0]
        self.home_lineup = create_lineup(home[3:14])
        self.away_lineup = create_lineup(away[3:14])
        self.home_corner_takers = home[16:18]
        self.away_corner_takers = away[16:18]
        self.home_free_kick_takers = home[20:22]
        self.away_free_kick_takers = away[20:22]
        self.home_penalty_taker = home[24]
        self.away_penalty_taker = away[24]
        self.stadium_name = lineups[53]

class NewSimulator(Simulator):

    def __init__(self, home_name: str, away_name: str, home_link: str, away_link: str) -> None:
        super().__init__(home_name, away_name)
        self.home_link = f'https://sofifa.com{home_link}'
        self.away_link = f'https://sofifa.com{away_link}'

    def scrape_team(self, link: str):
        """Given team name, scrape from SOFIFA all the necessary players and information about the lineup and set-piece takers."""
        fetch_html = fetch(link)
        soup = BeautifulSoup(fetch_html, "html.parser")
        info = soup.find("div", class_="bp3-card player").find("div", class_="card")
        players = soup.find("tbody")
        return {
            "info": info,
            "players": players
        }
    
    def get_starters(self, players: Tag):
        """Get the tags referring to the starters from the provided list of player tags."""
        starters = players.find_all("tr", class_="starting")
        result = []
        result_map = {}
        for starter in starters:
            name = starter.find("td", class_="col-name").find("a", role="tooltip").get_text()
            position = starter.find_all("td", class_="col-name")[1].find("span").get_text()
            rating = starter.find("td", class_="col col-oa").get_text()
            photo = starter.find("td", class_="col-avatar").find("img")["data-srcset"].split()[2]
            player = Player(name, position, rating, image=photo)
            result.append(player)
            result_map[name] = player
        return result, result_map
    
    def info_helper(self, info):
        """Helper to fetch section of SOFIFA squad that lists non-lineup information."""
        return info.find("ul", class_="pl").find_all("li")

    def get_set_piece_taker(self, info, teamType: TeamType, start: int, end = None):
        if end and start == end:
            scraped_taker = self.info_helper(info)[start]
            return self.home_away_map[teamType][scraped_taker.find("a").get_text()]
        scraped_takers = []
        if end:
            scraped_takers = self.info_helper(info)[start:end]
        else:
            scraped_takers = self.info_helper(info)[start:]
        result = []
        for taker in scraped_takers:
            result.append(self.home_away_map[teamType][taker.find("a").get_text()])
        return result
        
    def get_corner_takers(self, info, teamType: TeamType):
        """Fetch the corner kick takers for the team."""
        return self.get_set_piece_taker(info, teamType, -2)

    def get_free_kick_takers(self, info, teamType: TeamType):
        """Fetch the free kick takers for the team."""
        return self.get_set_piece_taker(info, teamType, 9, 11)

    def get_penalty_kick_taker(self, info, teamType: TeamType):
        """Fetch the penalty taker for the team."""
        return self.get_set_piece_taker(info, teamType, -3, -3)

    def get_stadium(self, info):
        """Fetch the stadium for the match."""
        stadium_name = self.info_helper(info)[0]
        stadium_name.find("label").decompose()
        return stadium_name.get_text()
    
    def get_simulator_info(self):
        """Scrape SOFIFA for the lineups and extraneous information of each team to set up data for the simulator."""
        home_team = self.scrape_team(self.home_link)
        self.home_lineup, self.home_lineup_map = self.get_starters(home_team["players"])
        self.home_corner_takers = self.get_corner_takers(home_team["info"], TeamType.HOME)
        self.home_free_kick_takers = self.get_free_kick_takers(home_team["info"], TeamType.HOME)
        self.home_penalty_taker = self.get_penalty_kick_taker(home_team["info"], TeamType.HOME)
        away_team = self.scrape_team(self.away_link)
        self.away_lineup, self.away_lineup_map = self.get_starters(away_team["players"])
        self.away_corner_takers = self.get_corner_takers(away_team["info"], TeamType.AWAY)
        self.away_free_kick_takers = self.get_free_kick_takers(away_team["info"], TeamType.AWAY)
        self.away_penalty_taker = self.get_penalty_kick_taker(away_team["info"], TeamType.AWAY)
        self.stadium_name = self.get_stadium(home_team["info"])
