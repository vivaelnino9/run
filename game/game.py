import curses

from background.background import Background
from player.player import Player

from curses.textpad import rectangle


class Game:
    def __init__(self, height, width):
        self.height = height  # 30
        self.width = width  # 100
        self.window = curses.newwin(self.height, self.width, 0, 0)
        self.ground = self.height - 8
        self.background = Background(self.window)
        self.player = Player(self.window, self.ground - 1, 9)
        # self.score = 0

    def move(self, direction):
        pass

    def connect(self):
        curses.curs_set(0)
        self.window.keypad(1)

    def start(self):
        # rock position
        position = self.width - 3
        while True:
            try:
                self.draw(position)
                key = self.window.getch()

                if key == curses.KEY_UP:
                    self.player.jump()
                elif key == curses.KEY_DOWN:
                    self.player.lower()

                # temp rock behavior
                position -= 2
                if position <= 0:
                    position = self.width - 3

            except KeyboardInterrupt:
                break

    def draw(self, position):
        self.window.erase()
        self.window.border(0)  # Draw border
        self.window.timeout(100)

        self.window.hline(self.ground, 1, '-', self.width - 2)
        self.background.draw()
        self.player.draw()

        # incoming rock
        if position > 0:
            rectangle(self.window, self.ground - 3, position, self.ground, position + 2)


