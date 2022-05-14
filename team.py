from player import Player

class Team:

    def __init__(self, team_name: str, players: list[str], corners: list[str], freekicks: list[str], penalty: list[str]):
        self._team_name = team_name
        self._defenders, self._midfielders, self._forwards, self._goalies = 0, 0, 0, 0
        self._format_players(players)
        self._calculate_average_rating()
        self._corners = corners
        self._freekicks = freekicks
        self._penalty = penalty    
        
    def _format_players(self, players: list[str]) -> None:
        """Set the players of the team as a list of Player Objects."""
        formatted_players: list[Player] = []
        for player in players:
            player_attributes = player.split()
            position = player_attributes[0]
            name = player_attributes[1]
            rating = player_attributes[2]
            formatted_player = Player(name, position, rating)
            position_type = formatted_player.get_position_type()
            if position_type == 'D':
                self._defenders += 1
            elif position_type == 'M':
                self._midfielders += 1
            elif position_type == "F":
                self._forwards += 1
            else:
                self._goalies += 1
            formatted_players.append(formatted_player)
        self._players = formatted_players

    def _calculate_average_rating(self) -> None:
        """Calculate the average rating of the team's players."""
        self._rating = sum(player.get_rating() for player in self._players) / len(self._players)

    def get_team_name(self) -> str:
        """Getter for the name property of the Team object."""
        return self._team_name

    def get_average_rating(self) -> float:
        """Getter for the average rating property of the Team object."""
        return self._rating

    def get_forwards(self) -> int:
        """Getter for the number of forwards stored in the Team object."""
        return self._forwards

    def get_players(self):
        """Getter for the list of players associated with the Team object."""
        return self._players

    def get_corner_takers(self):
        """Getter for the corner takers associated with the Team object."""
        return self._corners

    def get_free_kick_takers(self):
        """Getter for the free kick takers associated with the Team object."""
        return self._freekicks
    
    def get_penalty_takers(self):
        """Getter for the penalty kick takers associated with the Team object."""
        return self._penalty

    def get_player(self, number: int) -> Player:
        """Get a player from the list of players based on index input."""
        return self._players[number]

    def calculate_position_ratings(self, pos: str) -> int:
        """Calculate the sum of the ratings of the players that share the same position as pos."""
        total_rating = 0
        for player in self._players:
            if(player.get_position_type() == pos):
                total_rating += player.get_rating()
        return total_rating