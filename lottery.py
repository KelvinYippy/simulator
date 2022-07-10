
from random import randint
from data import LondonBluesFC, RedDevilsUnited
from team import Team

class LotteryTicket:

    def __init__(self, team: Team, numbers: list[int]) -> None:
        self._chosen_numbers = numbers
        self._team = team
        self._team.budget -= 1

    @property
    def chosen_numbers(self):
        return self._chosen_numbers
    
    @property
    def team(self):
        return self._team

class Lottery:

    def __init__(self) -> None:
        self._ticket_collection: list[LotteryTicket] = []

    def add_ticket(self, ticket: LotteryTicket) -> None:
        self._ticket_collection.append(ticket)

    def simulate_draw(self):
        lottery_rewards = {
            0: 0,
            1: 2,
            2: 4,
            3: 8,
            4: 14,
            5: 22,
            6: 32
        }
        numbers = {}
        while len(numbers) < 6:
            number = randint(1, 100)
            if not number in numbers:
                numbers[number] = len(numbers) + 1
        for ticket in self._ticket_collection:
            count = 0
            for number in ticket.chosen_numbers:
                if number in numbers:
                    count += 1
            ticket.team.budget += lottery_rewards[count]

if __name__ == "__main__":
    lottery_ticket_1 = LotteryTicket(RedDevilsUnited, [2, 5, 18, 29, 68, 83])
    lottery_ticket_2 = LotteryTicket(LondonBluesFC, [3, 19, 73, 74, 87, 89])
    lottery = Lottery()
    lottery.add_ticket(lottery_ticket_1)
    lottery.add_ticket(lottery_ticket_2)
    lottery.simulate_draw()