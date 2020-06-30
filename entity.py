from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")


class Entity:
    """
    An abstract object to represent players, enemies, items, etc.
    """
    def __init__(
            self,
            x = 0,
            y = 0,
            char = "?",
            color: Tuple[int, int, int] = (255, 255, 255),
            name = "<unnamed>",
            blocks_movement = False,
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks_movement = blocks_movement

    def spawn(self: T, gamemap: GameMap, x, y) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone

    def move(self, dx, dy) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy
