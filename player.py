class Player:

    def __init__(self, name: str, position: str, rating: str):
        self._name = name
        self._position = position
        self._rating = int(rating)
        self._set_position_type(position)

    def _set_position_type(self, position: str) -> None:
        """Assigns the position type of a player to one of Goalkeeper, Defender, Midfielder, or Forward."""
        if('B' in position):
            self._position_type = 'D'
        elif('M' in position):
            self._position_type = 'M'
        elif('G' in position):
            self._position_type = 'G'
        else:
            self._position_type = 'F'

    def get_name(self) -> str:
        """Getter for the name property of a Player object."""
        return self._name

    def get_position_type(self) -> str:
        """Getter for the position type property of a Player object."""
        return self._position_type

    def get_rating(self) -> int:
        """Getter for the rating property of a Player object."""
        return self._rating