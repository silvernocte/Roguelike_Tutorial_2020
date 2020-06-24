from typing import Tuple


class Entity:
    """
    An abstract object to represent players, enemies, items, etc.
    """
    def __init__(self, x, y, char, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx, dy) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
