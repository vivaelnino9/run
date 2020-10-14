from background.background import *
from obstacles.obstacles import *
from player.player import Player


class Game:
    def __init__(self, height, width, difficulty):
        self.height = height
        self.width = width
        self.window = curses.newwin(self.height, self.width, 0, 0)

        self.sky_height = round(self.height // 2.7)
        self.water_height = round(self.height // 2.1)
        self.beach_height = self.height // 6

        self.sky = Sky(self.window.subwin(self.sky_height, self.width, 0, 0))
        self.water = Water(self.window.subwin(self.water_height, self.width, self.sky_height, 0))
        self.beach = Beach(self.window.subwin(self.beach_height, self.width, self.sky_height+self.water_height, 0))

        self.difficulty = ['easy', 'medium', 'hard'][difficulty]
        self.obstacles = Obstacles(self.water, self.difficulty)
        self.player = Player(self.water)
        # self.score = 0

        self.connect()

    def move(self, direction):
        pass

    def connect(self):
        curses.curs_set(0)
        self.window.keypad(1)

    def start(self):
        while True:
            try:
                self.draw()
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

            except KeyboardInterrupt:
                break
        # print score

    def draw(self):
        self.window.erase()
        self.window.timeout(100)

        # Draw sub-windows
        self.sky.draw()
        self.water.draw()
        self.beach.draw()

        self.window.border(0)  # Draw border

        self.player.draw()  # Draw player
        self.obstacles.draw()  # Draw obstacles
