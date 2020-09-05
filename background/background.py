import curses, math, random


class Background:
    def __init__(self, window):
        self.window = window
        self.height, self.width = self.window.getmaxyx()
        self.ground = self.height - 20
        self.mountains = []
        self.clouds = []
        self.stars = []

        def get_clouds():
            for i in range(10):
                y, x = random.randrange(1, self.ground - 6), random.randrange(1, self.width - 15)
                self.clouds.append((y, x))

        get_clouds()

    def draw(self):
        # draw ground
        self.window.hline(self.ground, 1, '.', self.width - 2)
        # draw clouds
        self.draw_clouds()
        # draw mountains
        self.draw_mountains()

    def draw_stars(self):
        for s in self.stars:
            self.window.addstr(s[0], s[1], "*")

    def draw_clouds(self):
        for c in self.clouds:
            self.window.addstr(c[0], c[1], "    .,     ")
            self.window.addstr(c[0]+1, c[1], ";';'  ';'. ")
            self.window.addstr(c[0]+2, c[1], "';.,;    ,;")
            self.window.addstr(c[0]+3, c[1], "   '.';.'")

    def draw_mountains(self):
        if random.random() < .18:
            start, length = self.width - 1, random.randrange(1, 12, 2)
            new_mountain = Mountain(self.window, start, start + length, self.ground)
            self.mountains.append(new_mountain)

        for m in self.mountains:
            if m.end < 0:
                del m
            else:
                m.draw()
                m.move()


class Mountain():
    def __init__(self, window, start, end, base):
        self.start = start
        self.end = end
        self.base = base
        self.window = window

    def draw(self):
        height, width = self.window.getmaxyx()
        mountain = gen_mountain(self.start, self.end, self.base)
        for i in mountain:
            if 0 < i[0] < height and 0 < i[1] < width:
                self.window.addch(i[0], i[1], i[2])

    def move(self):
        self.start -= 1
        self.end -= 1


# TODO TRY TO SEE IF YOU CAN ADD CLOUDS
# class Cloud():


def gen_mountain(start, end, base_height):
    slope = math.ceil((end - start) / 2)

    y_list = list(range(base_height, base_height - slope, -1)) + list(range(base_height - slope + 1, base_height + 1))
    x_list = range(start, end+1)
    symbols = ['/'] * slope + ['\\'] * slope

    return list(zip(y_list, x_list, symbols))


# PYRAMID
# y, x = 22, 88
#
# for i in range(20):
#     uly, ulx = y + i, x - (i*2)
#     lry, lrx = (y+1) + i, (x+2) + (i*2)
#     pad.rectangle(win, uly, ulx, lry, lrx)
