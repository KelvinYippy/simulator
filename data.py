from player import Player
from stadium import Stadium
from team import Team
from training_ground import TrainingGround
from youth_academy import YouthAcademy
    
RedDevilsUnited = Team(
    "Red Devils United",
    120,
    TrainingGround(5),
    YouthAcademy(5),
    Stadium("Old Treatford", 10),
    "Erik Ten Hag",
    [
        Player("David De Gea", "GK", "84"),
        Player("Diogo Dalot", "RB", "77"),
        Player("Raphael Varane", "CB", "85"),
        Player("Frenkie De_Jong", "CM", "86"),
        Player("Bruno Fernandes", "AM", "86"),
        Player("Jadon Sancho", "LW", "85"),
        Player("Cristiano Ronaldo", "ST", "89")
    ]
)

LondonBluesFC = Team(
    "London Blues FC",
    100,
    TrainingGround(4),
    YouthAcademy(5),
    Stadium("Stratford Bridge", 9),
    "Thomas Tuchel",
    [
        Player("Edouard Mendy", "GK", "85"),
        Player("Reece James", "RB", "84"),
        Player("Thiago Silva", "CB", "85"),
        Player("Ngolo Kante", "CM", "86"),
        Player("Mason Mount", "AM", "85"),
        Player("Kai Havertz", "CF", "83"),
        Player("Romelu Lukaku", "ST", "87")
    ]
)