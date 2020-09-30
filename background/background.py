import curses, random

from background.boat import *


class Background:
    def __init__(self, window, rgb, id_start):
        self.window = window
        self.height, self.width = self.window.getmaxyx()

        self.rgb = rgb
        self.id_start = id_start

        self.initiate_colors()

    """
    Parameters: 
        window (curses.window): Window in which background is operating
        rgb (list): List of rgb values
        id_start (int): Number for start of color and color pair ids (below)
    
    Color Pair IDs (color pair: foreground/text and background color)
    ----------------
    Sky: 50 - 77 (including boat colors)
    Water: 100 - 113
    Beach: 200 - 205
    ----------------
    """

    def initiate_colors(self):
        # for each line initiate the color and pair for that line
        for y in range(self.height):
            color_id = self.id_start + y
            curses.init_color(color_id, self.rgb[0], self.rgb[1], self.rgb[2])
            curses.init_pair(color_id, curses.COLOR_WHITE, color_id)
            # For gradient effect, for each line decrement green and blue values by 4
            if self.rgb[0] > 4:
                self.rgb[0] -= 4
            if self.rgb[1] > 4:
                self.rgb[1] -= 4

    def draw(self):
        # for each line and column draw an empty string with the initiated color pair for that line
        for y in range(self.height):
            for x in range(self.width-1):
                self.window.addstr(y, x, ' ', curses.color_pair(self.get_color(y)))

    def get_color(self, y):
        # based on id start and current y position, return the color pair for that line
        return self.id_start + y


class Sky(Background):
    def __init__(self, window):
        Background.__init__(self, window, [40, 40, 40], 50)
        self.height, self.width = self.window.getmaxyx()  # 10, 100
        self.stars = []
        self.boats = []  # TODO LIST HERE MIGHT BE UNNECESSARY, KEEPING NOW FOR SIMPLICITY

        # generate first stars
        for i in range(20):
            self.add_star(random.randrange(1, self.width - 2))

        self.add_boat()

        # Boat Main Color
        curses.init_color(61, 131, 86, 41)
        # Boat Flag Color
        curses.init_color(71, 255, 50, 50)
        # Random Star Color
        curses.init_color(81, 250, 250, 0)

    def draw(self):
        super(Sky, self).draw()
        # TODO STAR AND BOAT DRAW FUNCTIONS VERY SIMILAR, MAYBE CAN BE CONDENSED
        self.draw_stars()
        self.draw_boats()

    def add_star(self, x=None):
        # create star object with coordinates y and x, if x not provided start it at the far right side of screen
        if x is None:
            x = self.width - 2
        y = random.randrange(1, self.height - 1)
        self.stars.append(Star(self, y, x))

    def draw_stars(self):
        # draw each star and move it left, if star reaches far left of screen remove it and add another.
        for s in self.stars:
            if s.x < 2:
                self.stars.remove(s)

            else:
                s.draw()
                s.move()
        if len(self.stars) < 20:
            self.add_star()

    def add_boat(self):
        self.boats.append(Boat(self, self.height-1, self.width-2))

    def draw_boats(self):
        # draw each boat and move it left, if boat reaches far left of screen remove it and add another.
        for b in self.boats:
            if b.x < b.end:
                self.boats.remove(b)
            else:
                b.draw()
                b.move()
        if len(self.boats) < 1:
            self.add_boat()


class Water(Background):
    def __init__(self, window):
        Background.__init__(self, window, [75, 75, 130], 100)


class Beach(Background):
    def __init__(self, window):
        Background.__init__(self, window, [240, 200, 160], 200)


class Boat:
    def __init__(self, sky, y, x):
        # TODO INITIATING THE COLOR PAIRS ON EACH DRAW SEEMS BAD, NEED A DIFFERENT SOLUTION
        self.sky = sky
        self.y = y
        self.x = x
        self.type = random.choice(['small_sail', 'big_sail'])
        # end: x coordinate when boat complete boat travels out of screen, signaling its removal
        self.end = -11 if self.type == 'small_sail' else -29

    def draw(self):
        y, x = self.y, self.x

        boat = draw_small_sail(y, x) if self.type == 'small_sail' else draw_big_sail(y, x)

        for part, details in boat.items():
            for d in details:
                if self.sky.width - 1 > d['x'] > 1:
                    if part == 'main':
                        color = 61 + d['y']
                        curses.init_pair(color, 61, self.sky.get_color(d['y']))
                    elif part == 'flag':
                        color = 71 + d['y']
                        curses.init_pair(color, 71, self.sky.get_color(d['y']))
                    else:
                        color = self.sky.get_color(d['y'])
                    self.sky.window.addstr(d['y'], d['x'], d['s'], curses.color_pair(color))

    def move(self):
        self.x -= 1


class Star:
    def __init__(self, sky, y, x):
        self.sky = sky
        self.y = y
        self.x = x

        self.color = self.sky.get_color(self.y)

        def initiate_color():
            # choose at random stars to be yellow instead of default white
            if random.randrange(0, 100) < 15:
                curses.init_pair(81 + self.y, 81, self.color)
                self.color = 81 + self.y

        initiate_color()

    def draw(self):
        self.sky.window.addstr(self.y, self.x, "*", curses.color_pair(self.color))

    def move(self):
        self.x -= 1

