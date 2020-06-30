import numpy as np  # type: ignore
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width, height):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.wall, order="F")

        self.visible = np.full((width, height), fill_value=False, order="F")  # Tiles currently in fov
        self.explored = np.full((width, height), fill_value=False, order="F") # Tiles player has seen before


    def in_bounds(self, x, y) -> bool:
        """Return True if x and y are inside the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map.
        If a tile is in the "visible" array, then draw it with "light" colors.
        If it isn't, but it's in the "explored" array, then draw it with "dark" colors.
        Otherwise, the default is "SHROUD".
        """
        console.tiles_rgb[0:self.width, 0:self.height] = np.select(
            condlist=[self.visible, self.explored],
            choicelist=[self.tiles["light"], self.tiles["dark"]],
            default=tile_types.SHROUD
        )
