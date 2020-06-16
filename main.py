import tcod

from actions import Action, ActionType
from input_handlers import handle_keys


def main():
    '''Main program function'''
    screen_width = 80
    screen_height = 50

    # set player initial position
    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    # set tcod to use the font image included in the project
    tcod.console_set_custom_font("arial10x10.png", tcod.FONT_TYPE_GREYSCALE | tcod.FONT_LAYOUT_TCOD)

    # set console parameters
    with tcod.console_init_root(
        w=screen_width,
        h=screen_height,
        title="The Worst Roguelike",
        order="F",
        vsync=True
    ) as root_console:
        # main loop
        while True:
            #draw '@'
            root_console.print(x=player_x, y=player_y, string="@")

            # print to console
            tcod.console_flush()

            # clear previous console
            root_console.clear()

            # wait for input
            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit()

                if event.type == "KEYDOWN":
                    action: [Action, None] = handle_keys(event.sym)

                    if action is None:
                        continue

                    action_type: ActionType = action.action_type

                    if action_type == ActionType.MOVEMENT:
                        dx = action.kwargs.get("dx", 0)
                        dy = action.kwargs.get("dy", 0)

                        player_x += dx
                        player_y += dy
                    elif action_type == ActionType.ESCAPE:
                        raise SystemExit()


if __name__ == '__main__':
    main()
