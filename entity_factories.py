from components.ai import HostileEnemy
from components.fighter import Fighter
from entity import Actor

player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=30, defense=2, power=5),
)

pixie = Actor(
    char="p",
    color=(217, 65, 194),
    name="Pixie",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=10, defense=0, power=3),
)

goblin = Actor(
    char="g",
    color=(0, 127, 0),
    name="Goblin",
    ai_cls=HostileEnemy,
    fighter=Fighter(hp=16, defense=1, power=4),
)