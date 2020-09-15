import curses, random


class Background:
    def __init__(self, window, rgb):
        self.window = window
        self.height, self.width = self.window.getmaxyx()
        self.rgb = rgb

    #  TODO INITIATE COLORS FIRST
    def draw(self, color=curses.COLOR_WHITE):
        if self.rgb:
            i = self.rgb[3]  # multiplier for color/pair identification. All colors and pairs need different ids
            for y in range(self.height):
                curses.init_color(y+i, self.rgb[0] + (y*5), self.rgb[1] + (y*5), self.rgb[2])
                curses.init_pair(y+i, color, y+i)
                for x in range(99):
                    self.window.addstr(y, x, ' ', curses.color_pair(y+i))

    def get_color(self, y):
        return y + self.rgb[3]


class Sky(Background):
    def __init__(self, window):
        Background.__init__(self, window, [0, 0, 0, 50])
        self.height, self.width = self.window.getmaxyx()  # 10, 100
        self.mountains = []
        self.clouds = []
        self.stars = []

        for i in range(20):
            self.add_star(random.randrange(1, self.width - 2))

    def draw(self, color=curses.COLOR_WHITE):
        super(Sky, self).draw()
        self.draw_stars()

    def add_star(self, x=98):
        y = random.randrange(1, self.height - 1)
        self.stars.append(Star(self.window, y, x))

    def draw_stars(self):
        for s in self.stars:
            if s.x < 2:
                self.stars.remove(s)

            else:
                s.draw()
                s.move()
        if len(self.stars) < 20:
            self.add_star()


class Water(Background):
    def __init__(self, window):
        Background.__init__(self, window, [10, 10, 115, 100])


class Beach(Background):
    def __init__(self, window):
        Background.__init__(self, window, [210, 180, 140, 200])


class Star:
    def __init__(self, window, y, x):
        self.window = window
        self.y, self.x = y, x

    def draw(self):
        self.window.addstr(self.y, self.x, "*")

    def move(self):
        self.x -= 1
