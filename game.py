from random import choice, choices, randint
from injury import Injury
from lineup import Lineup
from player import Player
from stadium import Stadium

from constants import scenarios

class Game:

    def __init__(self, home: Lineup, away: Lineup, neutral: bool, stadium: Stadium):
        self._home = home
        self._away = away
        self._neutral = neutral
        self._stadium = stadium
        self._calculate_goals()
        self._calculate_shots()
        self._calculate_injury()
        self._get_commentary()

    def _generate_random_factor(self, win: bool) -> list[int]:
        """Generates a random multiplier to be applied in the calculation of the number of goals the team scores."""
        if win:
            possible = [0, 1, 2, 3, 4, 5]
            return choices(possible, cum_weights=(10, 30, 50, 70, 90, 100), k=1)
        else:
            possible = [0, 1, 2, 3, 4]
            return choices(possible, cum_weights=(25, 50, 70, 85, 100), k=1)

    def _calculate_goals(self):
        """Calculate the number of goals that each team scores and assigns them as instance properties of the Game object."""
        home_weight, away_weight = 0,0
        home_goals, away_goals = 0,0
        home_rating, away_rating, stadium_level = self._home.rating, self._away.rating, self._stadium.level
        if self._neutral:
            home_weight = home_rating / away_rating
            away_weight = away_rating / home_rating
        else:
            home_weight = (home_rating + (stadium_level / 11)) / away_rating
            away_weight = away_rating / (home_rating + (stadium_level / 11))
        if home_weight > away_weight:
            home_goals = home_weight * self._generate_random_factor(True)[0]
            away_goals = away_weight * self._generate_random_factor(False)[0]
        elif away_weight > home_weight:
            home_goals = home_weight * self._generate_random_factor(False)[0]
            away_goals = away_weight * self._generate_random_factor(True)[0]
        else:
            home_goals, away_goals = home_weight * self._generate_random_factor(False)[0], away_weight * self._generate_random_factor(False)[0]
        self._home_goals, self._away_goals = int(home_goals), int(away_goals)

    def _calculate_shots(self):
        """Calculates the number of shots each team takes based on their defender and forward ratings, and sets them as instance properties of the Game object."""
        home_attack_rating = self._home.calculate_position_ratings('F')
        home_defender_rating = self._home.calculate_position_ratings('D')
        away_attack_rating = self._away.calculate_position_ratings('F')
        away_defender_rating = self._away.calculate_position_ratings('D')
        self._home_shots = int(self._home_goals + home_attack_rating / away_defender_rating + randint(0, self._home.forwards * 2))
        self._away_shots = int(self._away_goals + away_attack_rating / home_defender_rating + randint(0, self._away.forwards * 2))

    def _calculate_injury(self):
        """Calculates if any team has suffered an injury, and sets that as an instance property of the Game object."""
        h_factor, a_factor = randint(1,5), randint(1,5)
        if(h_factor == 1):
            player_injured = self._home.get_player(randint(1,10))
            self._home_injury = Injury(player_injured)
        else:
            self._home_injury = None
        if(a_factor == 1):
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

    def _get_commentary(self):
        """Generate commentary detailing all the goals occuring in a match, and sets that as instance property on the Game object."""
        minutes_array = self._get_minutes(self._home_goals + self._away_goals)
        events_array = []
        home_goals = self._home_goals
        away_goals = self._away_goals
        for minute in minutes_array:
            h_or_a = randint(0,1)
            event = ""
            scenario_number = randint(0, 8)
            if away_goals == 0 or (h_or_a == 1 and home_goals != 0):
                scenario = self._format_event(self._home.players, scenario_number, self._home.corner_takers, self._home.free_kick_takers, self._home.penalty_taker)
                event = f"{minute}: {scenario}"
                home_goals -= 1
            else:
                scenario = self._format_event(self._away.players, scenario_number, self._away.corner_takers, self._away.free_kick_takers, self._away.penalty_taker)
                event = f"{minute}: {scenario}"
                away_goals -= 1
            events_array.append(event)
        self._events = events_array

    def _format_event(self, players: list[Player], event, corners, freekicks, penalty):
        """Fetches desired scenario from the list of available scenarios and replaces content with the players involved. Returns this modified string."""
        scenario = scenarios[event]
        if(event < 2):
            crosser = choice(corners)
            scorer = players[randint(1,10)]
            while(crosser == scorer):
                scorer = players[randint(1,10)]
            amodified = scenario.replace('Assist', crosser)
            smodified = amodified.replace('Scorer', scorer.name)
            return smodified
        elif(event < 4):
            player = players[randint(1,10)]
            scorer = penalty
            pmodified = scenario.replace('Player', player.name)
            if(player.name == scorer):
                smodified = pmodified.replace('Scorer', f"{scorer} himself")
            else:
                smodified = pmodified.replace('Scorer', scorer)
            return smodified
        elif(event < 6):
            passer = list(filter(lambda player: (player.position_type == 'M'), players))
            chosenpasser = choice(passer)
            scorer = list(filter(lambda player: (player.position_type == 'F'), players))
            chosenscorer = choice(scorer)
            amodified = scenario.replace('Assist', chosenpasser.name)
            smodified = amodified.replace('Scorer', chosenscorer.name)
            return smodified
        elif(event < 8):
            passer = list(filter(lambda player: (player.position_type == 'M'), players))
            chosenpasser = choice(passer)
            scorer = list(filter(lambda player: (player.position_type == 'F'), players))
            chosenscorer = choice(scorer)
            amodified = scenario.replace('Assist', chosenpasser.name)
            smodified = amodified.replace('Scorer', chosenscorer.name)
            return smodified
        elif(event < 9):
            player = players[randint(1,10)]
            scorer = freekicks[randint(0,1)]
            pmodified = scenario.replace('Player', player.name)
            if(player.name == scorer):
                smodified = pmodified.replace('Scorer', f"{scorer} himself")
            else:
                smodified = pmodified.replace('Scorer', scorer)
            return smodified
        else:
            return scenario

    def __str__(self):
        goals = f"{self._home.team_name} {self._home_goals} - {self._away_goals} {self._away.team_name}"
        shots = f"Shots: {self._home_shots} - {self._away_shots}"
        home_injury, away_injury = "", ""
        if(self._home_injury):
            home_injury = str(self._home_injury)
        else:
            home_injury = "No injury for home team."
        if(self._away_injury):
            away_injury = str(self._away_injury)
        else:
            away_injury = "No injury for away team."
        goal_commentary = ""
        for i, event in enumerate(self._events):
            goal_commentary += event
            if(i != len(self._events) - 1):
                goal_commentary += "\n"
        return f"{goals}\n{shots}\n{home_injury} {away_injury}\n{goal_commentary}\n{self._stadium}"
