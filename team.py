class Team:

    def __init__(self, name: str, budget: int, training_ground, youth_academy, stadium, manager, players) -> None:
        self._name = name
        self._budget = budget
        self._training_ground_level = training_ground
        self._youth_academy = youth_academy
        self._stadium = stadium
        self._manager = manager
        self._players = players

    @property
    def name(self):
        return self._name

    @property
    def budget(self):
        return self._budget

    @budget.setter
    def budget(self, new_budget: int):
        self._budget = new_budget

    def __str__(self) -> str:
        pass

