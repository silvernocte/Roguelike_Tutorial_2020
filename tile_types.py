from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes for rgb colors.
        ("bg", "3B"),
    ]
)

# Tile scruct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", np.bool),  # True if this tile can be walked over.
        ("transparent", np.bool),  # True if this tile doesn't block FoV.
        ("dark", graphic_dt),  # Graphics for when this tile is out of FoV.
        ("light", graphic_dt),  # Graphics for when the tile is in FoV.
    ]
)


def new_tile(
        *,  # Enforce the use of keywords, so that parameter doesn't matter.
        walkable: int,
        transparent: int,
        dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
        light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.array:
    """Helper function for defining individual tile types"""
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(" "), (255, 255, 255), (80, 30, 4)),
    light=(ord(" "), (255, 255, 255), (100, 50, 4)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord(" "), (255, 255, 255), (50, 23, 2)),
    light=(ord(" "), (255, 255, 255), (79, 23, 2)),
)
