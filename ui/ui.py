import curses

from game.game import Game
from ui.menu import Menu


class Ui:
    def __init__(self, state, error, height, width):
        self.state = state  # 0: start, 2: controls, 4: exit
        self.error = error
        self.height = height
        self.width = width

        curses.curs_set(0)
        curses.noecho()

        self.window = curses.newwin(self.height, self.width, 0, 0)
        self.window.timeout(0)

    def run(self):
        while True:
            if self.state == -1:
                self.draw_background()
                self.draw_footer()
                self.window.getch()
                # start main menu
                m = Menu()
                if m.selection < 0:
                    break
                self.state = m.selection
            elif self.state == 0:
                self.window.erase()
                self.draw_footer(main=False)
                self.window.getch()
                # get game difficulty
                m = Menu(main=False)
                if m.selection < 0:
                    # go back to main menu
                    self.state = -1
                    continue
                # start game
                game = Game(self.height, self.width, difficulty=m.selection)
                game.start()
                # If quit game back to main menu
                self.state = -1
            elif self.state == 2:
                # TODO Controls State
                break
            elif self.state == 4:
                # TODO Exit State (Message for exiting)
                break

    def draw_background(self):
        rgb = [0, 250, 15]
        for i in range(16):
            curses.init_color(i+10, rgb[0], rgb[1] + (i*15), rgb[2] + (i*15))
            curses.init_pair(i+10, i+10, curses.COLOR_BLACK)

        self.window.border(0)
        self.window.bkgd(' ', curses.color_pair(9) | curses.A_BOLD)

        self.window.addstr(2, 17, "RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUU NNNNNNNN        NNNNNNNN", curses.color_pair(10))
        self.window.addstr(3, 17, "R::::::::::::::::R  U::::::U     U:::::U N:::::::N       N::::::N", curses.color_pair(11))
        self.window.addstr(4, 17, "R::::::RRRRRR:::::R U::::::U     U:::::U N::::::::N      N::::::N", curses.color_pair(12))
        self.window.addstr(5, 17, "RR:::::R     R:::::R U:::::U     U:::::U N:::::::::N     N::::::N", curses.color_pair(13))
        self.window.addstr(6, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::::::N    N::::::N", curses.color_pair(14))
        self.window.addstr(7, 17, "  R::::R     R:::::R U:::::U     U:::::U N:::::::::::N   N::::::N", curses.color_pair(15))
        self.window.addstr(8, 17, "  R::::RRRRRR:::::R  U:::::U     U:::::U N:::::::N::::N  N::::::N", curses.color_pair(16))
        self.window.addstr(9, 17, "  R:::::::::::::RR   U:::::U     U:::::U N::::::N N::::N N::::::N", curses.color_pair(17))
        self.window.addstr(10, 17, "  R::::RRRRRR:::::R  U:::::U     U:::::U N::::::N  N::::N:::::::N", curses.color_pair(18))
        self.window.addstr(11, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::N   N:::::::::::N", curses.color_pair(19))
        self.window.addstr(12, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::N    N::::::::::N", curses.color_pair(20))
        self.window.addstr(13, 17, "  R::::R     R:::::R U::::::U   U::::::U N::::::N     N:::::::::N", curses.color_pair(21))
        self.window.addstr(14, 17, "RR:::::R     R:::::R U:::::::UUU:::::::U N::::::N      N::::::::N", curses.color_pair(22))
        self.window.addstr(15, 17, "R::::::R     R:::::R  UU:::::::::::::UU  N::::::N       N:::::::N", curses.color_pair(23))
        self.window.addstr(16, 17, "R::::::R     R:::::R    UU:::::::::UU    N::::::N        N::::::N", curses.color_pair(24))
        self.window.addstr(17, 17, "RRRRRRRR     RRRRRRR      UUUUUUUUU      NNNNNNNN         NNNNNNN", curses.color_pair(25))

    def draw_footer(self, main=True):
        self.window.addstr(0, (80 - len(self.error)) // 2, self.error)
        self.window.addstr(27, 28, f' Move: ↓↑ | Select: Enter | {"Exit" if main else "Back"}: Ctrl + C')
