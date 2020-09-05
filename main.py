import curses

from game.game import Game

sc = curses.initscr()

HEIGHT, WIDTH = 30, 100

while True:

    windowSize = sc.getmaxyx()

    if windowSize[0] < HEIGHT or windowSize[1] < WIDTH:
        # Add warning here
        break

    else:
        game = Game(HEIGHT, WIDTH)
        game.connect()
        game.start()
        break


sc.refresh()
curses.endwin()