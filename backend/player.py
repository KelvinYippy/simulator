from constants import position_hashmap

class Player:

    def __init__(self, name: str, position: str, rating: str, image: str = None, age: int = None):
        self._name = name
        self._position = position
        self._rating = int(rating)
        self._age = age
        self._image = image
        self._set_position_type(position)

    def _set_position_type(self, position: str) -> None:
        """Assigns the position type of a player to one of Goalkeeper, Defender, Midfielder, or Forward."""
        self._position_type = position_hashmap[position]

    @property
    def name(self):
        return self._name

    @property
    def position(self):
        return self._position

    @property
    def position_type(self):
        return self._position_type

    @property
    def rating(self):
        return self._rating

    @property
    def age(self):
        return self._age

    def __str__(self) -> str:
        return f"{self._position} - {self._name} ({self._age}) [{self._rating}]"
        