class Player:
    def __init__(self, window, y, x):
        self.window = window
        self.y = self.grounded_height = y
        self.x = x
        self.phase = 2
        self.jumping = False

    def draw(self):
        # jump
        if self.jumping and self.grounded_height - self.y < 8:
            self.y -= 1
        elif self.jumping and self.y == self.grounded_height - 8:
            self.jumping = False
        elif not self.jumping and self.y < self.grounded_height:
            self.y += 1

        # head
        self.window.addch(self.y - 1, self.x, 'O')

        # torso
        self.window.addch(self.y, self.x, 'Ÿ')

        if self.jumping:
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

    def jump(self):
        if not self.jumping:
            self.jumping = True

    def lower(self):
        if self.jumping:
            self.jumping = False
