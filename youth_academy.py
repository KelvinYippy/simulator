from player import Prospect
from random import choices, randint
from constants import first_names, last_names

class YouthAcademy:

    def __init__(self, level: int) -> None:
        self._level = level

    def _generate_age(self) -> list[int]:
        potential_ages = [15, 16, 17, 18, 19]
        return choices(potential_ages, cum_weights=(15, 35, 65, 85, 100), k=1)

    def _generate_position(self) -> list[str]:
        potential_positions = ['GK', 'LWB', 'LB', 'CB', 'RB', 'RWB', 'DM', 'CM', 'LM', 'RM', 'AM', 'LW', 'ST', 'RW', 'CF']
        return choices(potential_positions, cum_weights=(11.25, 14.25, 21.75, 33, 40.5, 43.5, 51, 62.25, 66.25, 70.25, 77.75, 81.75, 93, 97, 100), k=1)

    def _generate_rating(self) -> int:
        rating_map = {
            1: randint(40, 50),
            2: randint(42, 55),
            3: randint(45, 60),
            4: randint(48, 65),
            5: randint(50, 70)
        }
        return rating_map[self._level]

    def _generate_potential(self) -> int:
        potential_map = {
            1: randint(40, 75),
            2: randint(45, 80),
            3: randint(50, 85),
            4: randint(55, 90),
            5: randint(60, 95)
        }
        return potential_map[self._level]

    def _generate_name(self) -> str:
        random_first_name = first_names[randint(0, len(first_names) - 1)]
        random_last_name = last_names[randint(0, len(first_names) - 1)]
        return f"{random_first_name} {random_last_name}"

    def _generate_prospect(self) -> Prospect:
        age = self._generate_age()[0]
        position = self._generate_position()[0]
        name = self._generate_name()
        rating = 1
        potential = 0
        while rating > potential:
            rating = self._generate_rating()
            potential = self._generate_potential()
        return Prospect(name, position, rating, potential, age)

if __name__ == "__main__":
    youth_academy = YouthAcademy(5)
    youngsters = []
    for i in range(5):
        youngsters.append(youth_academy._generate_prospect())
    for youngster in youngsters:
        print(youngster)