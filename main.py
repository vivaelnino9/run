import curses

from game.game import Game
from ui.ui import Ui

sc = curses.initscr()

uiState = -1
uiError = ''  # might use later

HEIGHT, WIDTH = 30, 100

while True:
    ui = Ui(uiState, uiError)
    uiState = ui.state

    if uiState == 0:
        game = Game(HEIGHT, WIDTH)
        game.connect()
        game.start()
    elif uiState == 2:
        # Controls
        pass
    else:
        # Exit
        pass
    break


sc.refresh()
curses.endwin()
