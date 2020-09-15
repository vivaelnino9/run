import curses
from game.game import Game
from ui.ui import Ui


def main(stdscr):
    ui = Ui(-1, '')
    ui_state = ui.state

    if ui_state == 0:
        game = Game()
        game.start()


curses.wrapper(main)

