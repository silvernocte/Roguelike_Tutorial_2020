import tcod.event

from actions import Action, ActionType


def handle_keys(key) -> [Action, None]:
    action: [Action, None] = None

    # directional movement
    if key == tcod. event.K_UP:
        action = Action(ActionType.MOVEMENT, dx=0, dy=-1)
    elif key == tcod. event.K_DOWN:
        action = Action(ActionType.MOVEMENT, dx=0, dy=1)
    elif key == tcod.event.K_LEFT:
        action = Action(ActionType.MOVEMENT, dx=-1, dy=0)
    elif key == tcod.event.K_RIGHT:
        action = Action(ActionType.MOVEMENT, dx=1, dy=0)

    # 'esc' key closes program
    elif key == tcod.event.K_ESCAPE:
        action = Action(ActionType.ESCAPE)

    # catch for no valid key press
    return action
