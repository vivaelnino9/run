import curses

from background.background import *
from player.player import Player

# from curses.textpad import rectangle


class Game:
    def __init__(self):
        self.height = 30
        self.width = 100
        self.window = curses.newwin(self.height, self.width, 0, 0)

        self.sky = Sky(self.window.subwin(10, self.width, 0, 0))  # 0 - 10
        self.water = Water(self.window.subwin(14, self.width, 10, 0))  # 10 - 24
        self.beach = Beach(self.window.subwin(6, self.width, 24, 0))  # 24 - 30

        self.player = Player(self.water)
        # self.score = 0

        self.connect()

    def move(self, direction):
        pass

    def connect(self):
        curses.curs_set(0)
        self.window.keypad(1)

    def start(self):
        # rock position
        position = self.width - 5
        while True:
            try:
                self.draw(position)
                key = self.window.getch()

                if key == curses.KEY_UP:
                    self.player.jump()
                elif key == curses.KEY_DOWN:
                    self.player.lower()

                elif key == curses.KEY_RIGHT:
                    self.player.move_forwards()
                elif key == curses.KEY_LEFT:
                    self.player.move_backwards()

                # temp rock behavior
                position -= 2
                if position <= 0:
                    position = self.width - 5

            except KeyboardInterrupt:
                break

    def draw(self, position):
        self.window.erase()
        self.window.timeout(100)

        # Draw sub-windows
        self.sky.draw()
        self.water.draw()
        self.beach.draw()

        self.window.border(0)  # Draw border

        self.player.draw()  # Draw player

        # incoming rock
        # TODO THIS WILL BE ITS OWN CLASS, HERE TEMPORARILY
        def rectangle(water, uly, ulx, lry, lrx):
            win = water.window
            win.vline(uly + 1, ulx, curses.ACS_VLINE, lry - uly - 1)
            win.hline(uly, ulx + 1, curses.ACS_HLINE, lrx - ulx - 1, curses.color_pair(water.get_color(uly)))
            # win.hline(lry, ulx + 1, curses.ACS_HLINE, lrx - ulx - 1, curses.color_pair(5))
            win.vline(uly + 1, lrx, curses.ACS_VLINE, lry - uly - 1)
            win.addstr(uly, ulx, '┌', curses.color_pair(water.get_color(uly)))
            win.addstr(uly, lrx, '┐', curses.color_pair(water.get_color(uly)))
            # win.addstr(lry, lrx, '┘', curses.color_pair(5))
            # win.addstr(lry, ulx, '└', curses.color_pair(5))

        if position > 0:
            rectangle(self.water, 10, position, 14, position + 4)


