from random import choice

# Possible scenarios in a game.
scenarios = [
    "Assist with an inswinging corner... and it is thumped in by Scorer!",
    "Assist with an outswinging corner... and it is headed in by Scorer!",
    f"Player crosses into the box... that is a handball! Penalty!\nScorer stares down the keeper and begins his run up... and smashes it into the {choice(['net', 'goal'])}!",
    "Player beats his man and is fouled in the box! Penalty!\nScorer stares down the keeper and begins his run up... and smashes it past the keeper!",
    "Scorer sprints down the wing... quick one-two with Assist... and hits it first-time... and it is a goal!",
    "Assist has the ball outside the 18-yard box... beautifully picks out the run of Scorer... and it is Scorer who calmly slots it home past the goalkeeper!",
    "Too many men on the attack leaves the team open at the back... Assist has a 3 on 1 and plays it to Scorer... quick move past the defender, and smashes it past the keeper!",
    "Bad pass by the attack... Assist picks it up and threads the ball past the defensive line... Scorer is through one on one, and slots it home past the keeper!",
    f"Player beats his man and is whacked from behind... Scorer fancies this free kick... and he {choice(['bends', 'powers'])} it past the keeper!",
]

sofifa_dictionary = {
    'Manchester United': "https://sofifa.com/team/11/manchester-united/",
    'Manchester City': "https://sofifa.com/team/10/manchester-city/",
    'Chelsea': "https://sofifa.com/team/5/chelsea/",
    'Arsenal': "https://sofifa.com/team/1/arsenal/" 
}

first_names = [
    "Toni",
    "Luka",
    "Carlos",
    "David",
    "Ferland",
    "Dani",
    "Thibaut",
    "Karim",
    "Federico",
    "Sadio",
    "Virgil",
    "Andrew",
    "Trent",
    "Ibrahim",
    "Jordan",
    "Thiago",
    "Mohammed",
    "Luis"
]

last_names = [
    "Kroos",
    "Modric",
    "Casemiro",
    "Alaba",
    "Mendy",
    "Carvajal",
    "Courtois",
    "Benzema",
    "Valverde",
    "Mane",
    "Van Dijk",
    "Robertson",
    "Alexander-Arnold",
    "Konate",
    "Henderson",
    "Alcantara",
    "Salah",
    "Diaz"
]