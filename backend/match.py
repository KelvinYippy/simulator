from random import choice, choices, randint
from event import Event
from injury import Injury
from lineup import Lineup
from player import Player
from stadium import Stadium

from constants import scenarios

class Match:

    def __init__(self, home: Lineup, away: Lineup, neutral: bool, stadium: Stadium) -> None:
        self._home = home
        self._away = away
        self._neutral = neutral
        self._stadium = stadium
        self._calculate_goals()
        self._calculate_shots()
        self._calculate_injury()
        self._get_commentary()

    def _generate_random_factor(self, win: bool) -> int:
        """Generates a random multiplier to be applied in the calculation of the number of goals the team scores."""
        if win:
            possible = [0, 1, 2, 3, 4, 5]
            weights = (10, 30, 50, 70, 90, 100)
        else:
            possible = [0, 1, 2, 3, 4]
            weights = (25, 50, 70, 85, 100)
        return choices(possible, cum_weights=weights, k=1)[0]

    def _calculate_goals(self) -> None:
        """Calculate the number of goals that each team scores and assigns them as instance properties of the Game object."""
        home_weight, away_weight = 0, 0
        home_goals, away_goals = 0, 0
        home_rating, away_rating, stadium_level = self._home.rating, self._away.rating, self._stadium.level
        weight = 0 if self._neutral else stadium_level / 11
        home_weight = (home_rating + weight) / away_rating
        away_weight = away_rating / (home_rating + weight)
        home_random_factor = True if home_weight > away_weight else False
        away_random_factor = True if home_weight < away_weight else False
        home_goals = home_weight * self._generate_random_factor(home_random_factor)
        away_goals = away_weight * self._generate_random_factor(away_random_factor)
        self._home_goals, self._away_goals = int(home_goals), int(away_goals)

    def _calculate_shots(self) -> None:
        """Calculates the number of shots each team takes based on their defender and forward ratings, and sets them as instance properties of the Game object."""
        home_attack_rating = self._home.calculate_position_ratings('F')
        home_defender_rating = self._home.calculate_position_ratings('D')
        away_attack_rating = self._away.calculate_position_ratings('F')
        away_defender_rating = self._away.calculate_position_ratings('D')
        self._home_shots = int(self._home_goals + home_attack_rating / away_defender_rating + randint(0, self._home.forwards * 2))
        self._away_shots = int(self._away_goals + away_attack_rating / home_defender_rating + randint(0, self._away.forwards * 2))

    def _calculate_injury(self) -> None:
        """Calculates if any team has suffered an injury, and sets that as an instance property of the Game object."""
        h_factor, a_factor = randint(1,5), randint(1,5)
        if h_factor == 1:
            player_injured = self._home.get_player(randint(1,10))
            self._home_injury = Injury(player_injured)
        else:
            self._home_injury = None
        if a_factor == 1:
            player_injured = self._away.get_player(randint(1,10))
            self._away_injury = Injury(player_injured)
        else:
            self._away_injury = None

    def _get_minutes(self, goals: int) -> list[int]:
        """Generate and return an array of integers that indicate when goals occurs in a game."""
        minutes = {}
        while goals != 0:
            minute = randint(1, 90)
            while minute in minutes:
                minute = randint(1, 90)
            minutes[minute] = 1
            goals -= 1
        return sorted(minutes)

    def _get_commentary(self) -> None:
        """Generate commentary detailing all the goals occuring in a match, and sets that as instance property on the Game object."""
        minutes_array = self._get_minutes(self._home_goals + self._away_goals)
        events_array: list[Event] = []
        home_goals = self._home_goals
        away_goals = self._away_goals
        for minute in minutes_array:
            h_or_a = randint(0,1)
            scenario_number = randint(0, 8)
            if away_goals == 0 or (h_or_a == 1 and home_goals != 0):
                events_array.append(self._format_event(self._home.players, minute, scenario_number, self._home.corner_takers, self._home.free_kick_takers, self._home.penalty_taker, True))
                home_goals -= 1
            else:
                events_array.append(self._format_event(self._away.players, minute, scenario_number, self._away.corner_takers, self._away.free_kick_takers, self._away.penalty_taker, False))
                away_goals -= 1
        self._events = events_array

    @property
    def events(self):
        return self._events

    @property 
    def home_injury(self):
        return self._home_injury

    @property
    def away_injury(self):
        return self._away_injury

    @property
    def home_goals(self):
        return self._home_goals

    @property
    def away_goals(self):
        return self._away_goals

    def _format_event(self, players: list[Player], minute: int, event_number: int, corners: list[Player], freekicks: list[Player], penalty: Player, is_home: bool):
        """Fetches desired scenario from the list of available scenarios and replaces content with the players involved. Returns this modified string."""
        def filter_position(player: Player, positions: list[str]):
            return player.position in positions
        def modify_string(scenario: str, player_one: Player, player_one_word: str, player_two: Player):
            player_one_modified = scenario.replace(player_one_word, player_one)
            player_two_modified = player_one_modified.replace("Scorer", player_two)
            return player_two_modified
        scenario = scenarios[event_number]
        print(scenario, event_number)
        if event_number < 2:
            crosser = choice(corners)
            scorer = players[randint(1,10)]
            while crosser == scorer.name:
                scorer = players[randint(1,10)]
            print()
            commentary = modify_string(scenario, crosser.name, "Assist", scorer.name)
            return Event(minute, commentary, crosser, scorer, is_home)
        elif event_number < 6:
            passer = [player for player in players if filter_position(player, ['LWB', 'LB', 'RB', 'RWB', 'DM', 'LDM', 'RDM', 'CDM', 'CM', 'LM', 'RM', 'AM', 'LAM', 'RAM'])]
            chosenpasser = choice(passer)
            scorer = [player for player in players if filter_position(player, ['LW', 'ST', 'RW', 'CF', 'LS', 'RS'])]
            chosenscorer = choice(scorer)
            commentary = modify_string(scenario, chosenpasser.name, "Assist", chosenscorer.name)
            return Event(minute, commentary, chosenpasser, chosenscorer, is_home)
        elif event_number < 9:
            print(players, freekicks, penalty)
            player = players[randint(1,10)]
            scorer = freekicks[randint(0,1)] if event_number == 8 else penalty
            print(player, scorer)
            # player_string = f"{scorer} himself" if player.name == scorer.name else scorer.name
            commentary = modify_string(scenario, player.name, "Player", scorer.name)
            return Event(minute, commentary, None if player.name == scorer.name else player, scorer, is_home)

    def __str__(self):
        goals = f"{self._home.team_name} {self._home_goals} - {self._away_goals} {self._away.team_name}"
        shots = f"Shots: {self._home_shots} - {self._away_shots}"
        home_injury, away_injury = "", ""
        if self._home_injury:
            home_injury = str(self._home_injury)
        else:
            home_injury = "No injury for home team."
        if self._away_injury:
            away_injury = str(self._away_injury)
        else:
            away_injury = "No injury for away team."
        goal_commentary = ""
        for i, event in enumerate(self._events):
            goal_commentary += str(event)
            if i != len(self._events) - 1:
                goal_commentary += "\n"
        return f"{goals}\n{shots}\n{home_injury} {away_injury}\n{goal_commentary}\n{self._stadium}"
