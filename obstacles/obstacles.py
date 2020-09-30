import curses, random

SETTINGS = {
    'easy': -40,
    'medium': -30,
    'hard': -20
}


class Obstacles:
    def __init__(self, background, difficulty):
        self.background = background
        self.window = background.window
        self.window_height, self.window_width = self.window.getmaxyx()

        self.difficulty = difficulty
        self.obstacles = []
        # TODO THIS IS DUMB
        self.add_obstacle(self.window_height-4, self.window_width-5, self.window_height, self.window_width-2)

    def add_obstacle(self, uly, ulx, lry, lrx):
        self.obstacles.append(Obstacle(self.background, uly,  ulx, lry, lrx))

    def draw(self):
        for o in self.obstacles:
            if o.ulx <= 0:
                self.obstacles.remove(o)
            else:
                o.draw()
                o.move()

        if len(self.obstacles) < 5:
            # Difficulty determines probability of lower spacing between obstacles
            spacing = random.randrange(-100, SETTINGS[self.difficulty])

            rand_height = random.randrange(1, 100)
            if rand_height < 15:
                height = self.window_height - 8
            elif 15 <= rand_height < 25:
                height = self.window_height - 7
            elif 25 <= rand_height < 40:
                height = self.window_height - 6
            elif 40 <= rand_height < 60:
                height = self.window_height - 5
            else:
                height = self.window_height - 4

            if self.obstacles[-1].ulx <= self.window_width+spacing:
                self.add_obstacle(height, self.window_width - 5, self.window_height, self.window_width - 2)


class Obstacle:
    def __init__(self, background, uly, ulx, lry, lrx):
        self.background = background
        self.uly = uly
        self.ulx = ulx
        self.lry = lry
        self.lrx = lrx

    def draw(self):
        win = self.background.window
        win.vline(self.uly + 1, self.ulx, curses.ACS_VLINE, self.lry - self.uly - 1)
        win.hline(self.uly, self.ulx + 1, curses.ACS_HLINE, self.lrx - self.ulx - 1,
                  curses.color_pair(self.background.get_color(self.uly)))
        # win.hline(lry, ulx + 1, curses.ACS_HLINE, lrx - ulx - 1, curses.color_pair(5))
        win.vline(self.uly + 1, self.lrx, curses.ACS_VLINE, self.lry - self.uly - 1)
        win.addstr(self.uly, self.ulx, '┌', curses.color_pair(self.background.get_color(self.uly)))
        win.addstr(self.uly, self.lrx, '┐', curses.color_pair(self.background.get_color(self.uly)))
        # win.addstr(lry, lrx, '┘', curses.color_pair(5))
        # win.addstr(lry, ulx, '└', curses.color_pair(5))

    def move(self):
        self.ulx -= 2
        self.lrx -= 2
