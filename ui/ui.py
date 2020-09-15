import curses

from ui.menu import Menu


class Ui:
    def __init__(self, state, error):
        self.state = state  # 0: start, 2: controls, 4: exit
        self.error = error

        self.s = curses.initscr()
        curses.curs_set(0)
        curses.noecho()

        self.w = curses.newwin(30, 100, 0, 0)
        self.w.timeout(0)

        if self.state == -1:
            try:
                self.draw_background()
                self.w.getch()
                m = Menu()
                self.state = m.selection
            except KeyboardInterrupt:
                self.state = 1

        # TODO Controls State
        # TODO Exit State (Message for exiting)

    def draw_background(self):
        # TODO MOVE THIS TO MAIN.PY
        curses.start_color()
        curses.use_default_colors()

        for i in range(256):
            curses.init_pair(i + 1, i, -1)

        self.w.border(0)
        self.w.bkgd(' ', curses.color_pair(9) | curses.A_BOLD)

        self.w.addstr(2, 17, "RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUU NNNNNNNN        NNNNNNNN", curses.color_pair(23))
        self.w.addstr(3, 17, "R::::::::::::::::R  U::::::U     U:::::U N:::::::N       N::::::N", curses.color_pair(23))
        self.w.addstr(4, 17, "R::::::RRRRRR:::::R U::::::U     U:::::U N::::::::N      N::::::N", curses.color_pair(23))
        self.w.addstr(5, 17, "RR:::::R     R:::::R U:::::U     U:::::U N:::::::::N     N::::::N", curses.color_pair(23))
        self.w.addstr(6, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::::::N    N::::::N", curses.color_pair(29))
        self.w.addstr(7, 17, "  R::::R     R:::::R U:::::U     U:::::U N:::::::::::N   N::::::N", curses.color_pair(29))
        self.w.addstr(8, 17, "  R::::RRRRRR:::::R  U:::::U     U:::::U N:::::::N::::N  N::::::N", curses.color_pair(29))
        self.w.addstr(9, 17, "  R:::::::::::::RR   U:::::U     U:::::U N::::::N N::::N N::::::N", curses.color_pair(29))
        self.w.addstr(10, 17, "  R::::RRRRRR:::::R  U:::::U     U:::::U N::::::N  N::::N:::::::N", curses.color_pair(29))
        self.w.addstr(11, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::N   N:::::::::::N", curses.color_pair(35))
        self.w.addstr(12, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::N    N::::::::::N", curses.color_pair(35))
        self.w.addstr(13, 17, "  R::::R     R:::::R U::::::U   U::::::U N::::::N     N:::::::::N", curses.color_pair(35))
        self.w.addstr(14, 17, "RR:::::R     R:::::R U:::::::UUU:::::::U N::::::N      N::::::::N", curses.color_pair(41))
        self.w.addstr(15, 17, "R::::::R     R:::::R  UU:::::::::::::UU  N::::::N       N:::::::N", curses.color_pair(41))
        self.w.addstr(16, 17, "R::::::R     R:::::R    UU:::::::::UU    N::::::N        N::::::N", curses.color_pair(41))
        self.w.addstr(17, 17, "RRRRRRRR     RRRRRRR      UUUUUUUUU      NNNNNNNN         NNNNNNN", curses.color_pair(41))

        self.w.addstr(0, (80 - len(self.error)) // 2, self.error)
        self.w.addstr(27, 35, ' Move: ↓↑ | Select: Enter')