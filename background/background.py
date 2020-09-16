import curses, random


class Background:
    def __init__(self, window, rgb, id_start, text_color=curses.COLOR_WHITE):
        self.window = window
        self.height, self.width = self.window.getmaxyx()

        self.rgb = rgb
        self.id_start = id_start
        self.text_color = text_color

        self.initiate_colors()

    """
    Parameters: 
        window (curses.window): Window in which background is operating
        rgb (list): List of rgb values
        id_start (int): Number for start of color and color pair ids (below)
        text_color (int): Number of color id for text color, default white
    
    Color Pair IDs (color pair: foreground/text and background color)
    ----------------
    Sky: 50 - 59
    Water: 100 - 113
    Beach: 200 - 205
    ----------------
    """

    def initiate_colors(self):
        # for each line initiate the color and pair for that line
        for y in range(self.height):
            color_id = self.id_start + y
            curses.init_color(color_id, self.rgb[0], self.rgb[1], self.rgb[2])
            curses.init_pair(color_id, self.text_color, color_id)
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

        # generate first stars
        for i in range(20):
            self.add_star(random.randrange(1, self.width - 2))

    def draw(self, color=curses.COLOR_WHITE):
        super(Sky, self).draw()
        self.draw_stars()

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


class Water(Background):
    def __init__(self, window):
        Background.__init__(self, window, [75, 75, 130], 100)


class Beach(Background):
    def __init__(self, window):
        Background.__init__(self, window, [240, 200, 160], 200)


class Star:
    def __init__(self, sky, y, x):
        self.sky = sky
        self.y = y
        self.x = x

    def draw(self):
        self.sky.window.addstr(self.y, self.x, "*", curses.color_pair(self.sky.get_color(self.y)))

    def move(self):
        self.x -= 1
