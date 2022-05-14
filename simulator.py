import sys
from game import Game
from stadium import Stadium
from team import Team

class SoccerSimulator():

    def __init__(self, file: str) -> None:
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
    
    def run(self):
        """Main function to run the soccer simulator."""
        lineups = self._scan_lineup()
        home, away = lineups[0:25], lineups[26:51]
        home_name, away_name = home[0], away[0]
        home_lineup, away_lineup = home[3:14], away[3:14]
        home_corner_takers, away_corner_takers = home[16:18], away[16:18]
        home_free_kick_takers, away_free_kick_takers = home[20:22], away[20:22]
        home_penalty_taker, away_penalty_taker = home[24], away[24]
        stadium_info = lineups[53:55]
        home_team = Team(home_name, home_lineup, home_corner_takers, home_free_kick_takers, home_penalty_taker)
        away_team = Team(away_name, away_lineup, away_corner_takers, away_free_kick_takers, away_penalty_taker)
        venue = Stadium(stadium_info[0], int(stadium_info[1]))
        match = Game(home_team, away_team, False, venue)
        print(match)

if __name__ == "__main__":
    SoccerSimulator(sys.argv[1]).run()