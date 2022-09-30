from typing import Union
from player import Player

class Event:

    def __init__(self, minute: int, commentary: str, assister: Union[Player, str, None], scorer: Union[Player, str]) -> None:
        self._minute = minute
        self._commentary = commentary
        self._assister = assister
        self._scorer = scorer

    def __str__(self) -> str:
        return f"{self._minute}: {self._commentary}"