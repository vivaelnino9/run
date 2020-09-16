import curses
from game.game import Game
from ui.ui import Ui

HEIGHT = 30
WIDTH = 100


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    ui = Ui(-1, '', HEIGHT, WIDTH)
    ui_state = ui.state

    if ui_state == 0:
        game = Game(HEIGHT, WIDTH)
        game.start()


curses.wrapper(main)

