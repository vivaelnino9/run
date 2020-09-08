class Player:
    def __init__(self, window, y, x):
        self.window = window
        self.y = self.grounded_height = y
        self.x = x
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

        # TODO drawing can be done better here, maybe in a different place? Its own function?

        # head
        self.window.addch(self.y - 1, self.x, 'O')

        # torso
        self.window.addch(self.y, self.x, 'Ÿ')

        if self.is_jumping:
            # left arm
            self.window.addch(self.y - 1, self.x - 1, "\\")
            # right arm
            self.window.addch(self.y - 1, self.x + 1, "/")
        else:
            # left arm
            self.window.addch(self.y, self.x - 1, "/")
            # right arm
            self.window.addch(self.y, self.x + 1, "\\")

        if self.phase == 1:
            # left leg
            self.window.addch(self.y + 1, self.x - 1, '/')
            # right leg
            self.window.addch(self.y + 1, self.x + 1, "\\")
        elif self.phase == 2:
            # single leg
            self.window.addch(self.y + 1, self.x, '|')
        else:
            # left leg
            self.window.addch(self.y, self.x - 1, '/')

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

    def jump(self):
        """Puts the player in the jumping phase if it isn't but not when double jump isn't available"""
        if not self.is_jumping and self.double_jump_avail:
            self.is_jumping = True

    def lower(self):
        """Takes the player out of jumping phase if it is"""
        # TODO this needs to be improved, not very useful
        if self.is_jumping:
            self.is_jumping = False
