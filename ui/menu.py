import curses
from time import sleep


class Menu:
    def __init__(self, main=True, message=None):
        self.selection = 0
        self.message = message  # might use later
        # Labels specify if they are  selectable because I might add different types of labels like input or bool
        self.menu = [
            {'Label': 'START' if main else 'EASY', 'selectable': 1},
            {'Label': 'CONTROLS' if main else 'MEDIUM', 'selectable': 1},
            {'Label': 'EXIT' if main else 'HARD', 'selectable': 1}
        ]
        self.window = curses.newwin(7, 21, 19 if main else 12, 37)  # have difficulty menu start display center screen

        self.window.timeout(100)
        self.window.keypad(1)

        self.create_menu()

    def create_menu(self):
        # initiate menu colors
        curses.init_color(30, 400, 0, 0)
        curses.init_pair(30, 30, curses.COLOR_BLACK)

        while True:
            try:
                key = self.window.getch()

                if key == curses.KEY_UP:
                    if self.selection - 1 >= 0:
                        self.selection -= 1
                    else:
                        self.selection = len(self.menu) - 1

                elif key == curses.KEY_DOWN:
                    if self.selection + 1 <= len(self.menu) - 1:
                        self.selection += 1
                    else:
                        self.selection = 0

                elif key == 10:
                    if 'selectable' in self.menu[self.selection]:
                        self.select()
                        break
            except KeyboardInterrupt:
                self.selection = -1
                break

            self.draw()

    def draw(self):
        self.window.erase()
        self.window.bkgd(' ', curses.color_pair(30) | curses.A_BOLD)

        for index in range(0, len(self.menu)):
            checked = '>' if index == self.selection else ' '  # arrow next to highlighted selection
            self.window.addstr(2 * index, 5, f'{checked} {self.menu[index]["Label"]}', curses.color_pair(30))

    def select(self):
        label = self.menu[self.selection]['Label']
        index = self.selection

        for i in range(2):
            # Make selection blink when selected
            self.menu[index]['Label'] = ''
            self.draw()
            self.window.refresh()
            sleep(0.15)

            self.menu[index]['Label'] = label
            self.draw()
            self.window.refresh()
            sleep(0.15)