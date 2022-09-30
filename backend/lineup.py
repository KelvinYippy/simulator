from player import Player

class Lineup:

    def __init__(self, team_name: str, players: list[str], corner_takers: list[str], free_kick_takers: list[str], penalty_taker: str) -> None:
        self._team_name = team_name
        self._defenders, self._midfielders, self._forwards, self._goalies = 0, 0, 0, 0
        self._rating_dictionary = {
            "G": 0,
            "D": 0,
            "M": 0,
            "F": 0
        }
        self._format_players(players)
        self._calculate_average_rating()
        self._corner_takers = corner_takers
        self._free_kick_takers = free_kick_takers
        self._penalty_taker = penalty_taker    
        
    def _format_players(self, players: list[str]) -> None:
        """Set the players of the team as a list of Player Objects."""
        formatted_players: list[Player] = []
        for player in players:
            player_attributes = player.split()
            position = player_attributes.pop(0)
            rating = player_attributes.pop()
            name = " ".join(player_attributes)
            formatted_player = Player(name, position, rating)
            position_type, rating = formatted_player.position_type, formatted_player.rating
            if position_type == 'D':
                self._defenders += 1
            elif position_type == 'M':
                self._midfielders += 1
            elif position_type == "F":
                self._forwards += 1
            else:
                self._goalies += 1
            self._rating_dictionary[position_type] += rating
            formatted_players.append(formatted_player)
        self._players = formatted_players

    def _calculate_average_rating(self) -> None:
        """Calculate the average rating of the team's players."""
        self._rating = sum(player.rating for player in self._players) / len(self._players)

    @property
    def team_name(self) -> str:
        return self._team_name

    @property
    def rating(self) -> float:
        return self._rating

    @property
    def forwards(self) -> int:
        return self._forwards

    @property
    def players(self) -> list[Player]:
        return self._players

    @property
    def corner_takers(self) -> list[str]:
        return self._corner_takers

    @property
    def free_kick_takers(self) -> list[str]:
        return self._free_kick_takers

    @property
    def penalty_taker(self) -> str:
        return self._penalty_taker

    def get_player(self, number: int) -> Player:
        """Get a player from the list of players based on index input."""
        return self._players[number]

    def calculate_position_ratings(self, pos: str) -> int:
        """Fetch the total rating of the players that share the same position type as parameter pos"""
        return self._rating_dictionary[pos]