from random import randint

from player import Player

class Injury:

    def __init__(self, player: Player):
        self._player = player
        self._calculate_injury_length()

    def _calculate_injury_length(self) -> None:
        """Assigns the length of the player injury to a random integer between 1 and 7."""
        self._length = randint(1, 7)
    
    def __str__(self) -> str:
        return f"{self._player.get_name()} injured for {self._length} {'days' if self._length > 1 else 'day'}."