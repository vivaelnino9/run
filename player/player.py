import curses


class Player:
    def __init__(self, water):
        # TODO ADD SHADOW OF PLAYER ON BEACH. MAYBE THAT GOES HERE MAYBE NOT.
        self.water = water
        self.water_window = self.water.window
        self.water_height, self.water_width = self.water_window.getmaxyx()
        self.y = self.grounded_height = self.water_height-2
        self.x = 9

        self.phase = 2
        self.is_jumping = False
        self.double_jump_avail = True
        self.moving_up = False
        self.moving_down = False

    def draw(self):
        """Draws the player on the window taking into consideration its direction and action phase"""
        if not self.is_above_ground():
            # reset movement and double jump on ground
            self.moving_up = self.moving_down = False
            if not self.double_jump_avail:
                self.double_jump_avail = True

        if self.is_jumping:
            if not self.is_max_height():
                if self.moving_down:
                    # if we get here it means double jump has been made, now make it unavailable till we hit ground
                    self.moving_down = False
                    self.double_jump_avail = False
                self.y -= 1  # move player up
                self.moving_up = True
            else:
                self.is_jumping = False
        else:
            if self.is_above_ground():
                self.y += 1  # move player down
                self.moving_down = True
                self.moving_up = False

        # TODO DRAWING CAN BE DONE BETTER HERE, MAYBE IN A DIFFERENT PLACE? ITS OWN FUNCTION?
        # TODO NOW WITH COLORS BEING SPECIFIED THI REALLY NEEDS TO BE CLEANED UP

        # head
        self.water_window.addstr(self.y - 1, self.x, 'O', curses.color_pair(self.water.get_color(self.y-1)))

        # torso
        self.water_window.addstr(self.y, self.x, 'Ÿ', curses.color_pair(self.water.get_color(self.y)))

        if self.is_jumping:
            # left arm
            self.water_window.addstr(self.y - 1, self.x - 1, "\\", curses.color_pair(self.water.get_color(self.y-1)))
            # right arm
            self.water_window.addstr(self.y - 1, self.x + 1, "/", curses.color_pair(self.water.get_color(self.y-1)))
        else:
            # left arm
            self.water_window.addstr(self.y, self.x - 1, "/", curses.color_pair(self.water.get_color(self.y)))
            # right arm
            self.water_window.addstr(self.y, self.x + 1, "\\", curses.color_pair(self.water.get_color(self.y)))

        if self.phase == 1:
            # left leg
            self.water_window.addstr(self.y + 1, self.x - 1, '/', curses.color_pair(self.water.get_color(self.y+1)))
            # right leg
            self.water_window.addstr(self.y + 1, self.x + 1, "\\", curses.color_pair(self.water.get_color(self.y+1)))
        elif self.phase == 2:
            # single leg
            self.water_window.addstr(self.y + 1, self.x, '|', curses.color_pair(self.water.get_color(self.y+1)))
        else:
            # left leg
            self.water_window.addstr(self.y, self.x - 1, '/', curses.color_pair(self.water.get_color(self.y)))

        if self.phase < 3:
            self.phase += 1
        else:
            self.phase = 1

    def is_above_ground(self):
        """Checks if player is above ground"""
        return self.y < self.grounded_height

    def is_max_height(self):
        """Checks if player is at maximum height (where background starts)"""
        return self.y == self.grounded_height - 8

    def move_forwards(self):
        if self.x < self.water_width - 4:
            self.x += 3

    def move_backwards(self):
        if self.x > 4:
            self.x -= 3

    def jump(self):
        """Puts the player in the jumping phase if it isn't but not when double jump isn't available"""
        if not self.is_jumping and self.double_jump_avail:
            self.is_jumping = True

    def lower(self):
        """Takes the player out of jumping phase if it is"""
        # TODO this needs to be improved, not very useful
        if self.is_jumping:
            self.is_jumping = False
