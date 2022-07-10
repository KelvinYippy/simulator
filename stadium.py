from random import randint

class Stadium:

    def __init__(self, stadium_name: str, level: int) -> None:
        self._stadium_name = stadium_name
        self._level = level
        self._calculate_attendance()

    def _calculate_attendance(self) -> None:
        """Assigns attendance of the game to be a random integer between 10000 times one less the current level and 10000 times the current level."""
        self._attendance = randint((self._level - 1) * 10000, self._level * 10000)

    @property
    def level(self):
        return self._level

    def __str__(self) -> str:
        return f"{self._stadium_name} - Attendance: {self._attendance}"