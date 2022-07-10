from random import randint
from team import Team
from data import RedDevilsUnited

class Roulette:

    def __init__(self) -> None:
        pass

    def simulate_draw(self, team: Team, stake: int, color: str) -> None:
        result = randint(1, 38)
        if result > 36:
            team.budget -= stake
        else:
            if (result % 2 == 0 and color == "B") or (result % 2 == 1 and color == "R"):
                team.budget += (stake * 2)
            else:
                team.budget -= stake
        print(f"{team.name} has budget: {team.budget}")

if __name__ == "__main__":
    roulette = Roulette()
    roulette.simulate_draw(RedDevilsUnited, 5, "B")