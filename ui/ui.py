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
        rgb = [0, 250, 15]
        for i in range(16):
            curses.init_color(i+10, rgb[0], rgb[1] + (i*15), rgb[2] + (i*15))
            curses.init_pair(i+10, i+10, curses.COLOR_BLACK)

        self.w.border(0)
        self.w.bkgd(' ', curses.color_pair(9) | curses.A_BOLD)

        self.w.addstr(2, 17, "RRRRRRRRRRRRRRRRR   UUUUUUUU     UUUUUUU NNNNNNNN        NNNNNNNN", curses.color_pair(10))
        self.w.addstr(3, 17, "R::::::::::::::::R  U::::::U     U:::::U N:::::::N       N::::::N", curses.color_pair(11))
        self.w.addstr(4, 17, "R::::::RRRRRR:::::R U::::::U     U:::::U N::::::::N      N::::::N", curses.color_pair(12))
        self.w.addstr(5, 17, "RR:::::R     R:::::R U:::::U     U:::::U N:::::::::N     N::::::N", curses.color_pair(13))
        self.w.addstr(6, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::::::N    N::::::N", curses.color_pair(14))
        self.w.addstr(7, 17, "  R::::R     R:::::R U:::::U     U:::::U N:::::::::::N   N::::::N", curses.color_pair(15))
        self.w.addstr(8, 17, "  R::::RRRRRR:::::R  U:::::U     U:::::U N:::::::N::::N  N::::::N", curses.color_pair(16))
        self.w.addstr(9, 17, "  R:::::::::::::RR   U:::::U     U:::::U N::::::N N::::N N::::::N", curses.color_pair(17))
        self.w.addstr(10, 17, "  R::::RRRRRR:::::R  U:::::U     U:::::U N::::::N  N::::N:::::::N", curses.color_pair(18))
        self.w.addstr(11, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::N   N:::::::::::N", curses.color_pair(19))
        self.w.addstr(12, 17, "  R::::R     R:::::R U:::::U     U:::::U N::::::N    N::::::::::N", curses.color_pair(20))
        self.w.addstr(13, 17, "  R::::R     R:::::R U::::::U   U::::::U N::::::N     N:::::::::N", curses.color_pair(21))
        self.w.addstr(14, 17, "RR:::::R     R:::::R U:::::::UUU:::::::U N::::::N      N::::::::N", curses.color_pair(22))
        self.w.addstr(15, 17, "R::::::R     R:::::R  UU:::::::::::::UU  N::::::N       N:::::::N", curses.color_pair(23))
        self.w.addstr(16, 17, "R::::::R     R:::::R    UU:::::::::UU    N::::::N        N::::::N", curses.color_pair(24))
        self.w.addstr(17, 17, "RRRRRRRR     RRRRRRR      UUUUUUUUU      NNNNNNNN         NNNNNNN", curses.color_pair(25))

        self.w.addstr(0, (80 - len(self.error)) // 2, self.error)
        self.w.addstr(27, 35, ' Move: ↓↑ | Select: Enter')
