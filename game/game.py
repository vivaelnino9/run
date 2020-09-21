import curses

from background.background import *
from player.player import Player

# from curses.textpad import rectangle


class Game:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.window = curses.newwin(self.height, self.width, 0, 0)

        self.sky_height = round(self.height // 2.7)
        self.water_height = round(self.height // 2.1)
        self.beach_height = self.height // 6

        self.sky = Sky(self.window.subwin(self.sky_height, self.width, 0, 0))
        self.water = Water(self.window.subwin(self.water_height, self.width, self.sky_height, 0))
        self.beach = Beach(self.window.subwin(self.beach_height, self.width, self.sky_height+self.water_height, 0))

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
                self.window.refresh()
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
            rectangle(self.water, 10, position, self.water_height, position + 4)


