import curses
from ui.ui import Ui

# IN THE FUTURE THIS COULD BE AN OPTIONAL INPUT?
HEIGHT = 30
WIDTH = 100


def main(stdscr):
    curses.start_color()
    curses.use_default_colors()

    ui = Ui(-1, '', HEIGHT, WIDTH)
    ui.run()


curses.wrapper(main)
