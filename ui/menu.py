import curses
from time import sleep


class Menu:
    def __init__(self, message=None):
        self.w = curses.newwin(7, 21, 19, 37)
        self.selection = 0
        self.message = message  # might use later
        # Labels specify if they are  selectable because I might add different types of labels like input or bool
        self.menu = [
            {'Label': 'START', 'selectable': 1},
            {'Label': '', 'skip': True},
            {'Label': 'CONTROLS', 'selectable': 1},
            {'Label': '', 'skip': True},
            {'Label': 'EXIT', 'selectable': 1}
        ]

        self.w.timeout(100)
        self.w.keypad(1)
        self.w.border(0)

        self.create_menu()

    def create_menu(self):
        while True:
            key = self.w.getch()

            if key == curses.KEY_UP:
                index = self.selection
                while True:
                    if index - 1 >= 0 and 'skip' in self.menu[index - 1]:
                        index -= 1
                    elif index - 1 >= 0:
                        index -= 1
                        break
                    else:
                        break
                self.selection = index

            elif key == curses.KEY_DOWN:
                index = self.selection
                while True:
                    if index + 1 <= len(self.menu) - 1 and 'skip' in self.menu[index + 1]:
                        index += 1
                    elif index + 1 <= len(self.menu) - 1:
                        index += 1
                        break
                    else:
                        break
                self.selection = index

            elif key == 10:
                if 'selectable' in self.menu[self.selection]:
                    self.select()
                    break

            self.draw()

    def draw(self):
        self.w.erase()
        self.w.bkgd(' ', curses.color_pair(125) | curses.A_BOLD)

        for index in range(0, len(self.menu)):
            checked = '>' if index == self.selection else ' '  # arrow next to highlighted selection
            self.w.addstr(1 + index, 5, f'{checked} {self.menu[index]["Label"]}', curses.color_pair(125) |
                          curses.A_BLINK)

    def select(self):
        label = self.menu[self.selection]['Label']
        index = self.selection

        for i in range(2):
            # Make selection blink when selected
            self.menu[index]['Label'] = ''
            self.draw()
            self.w.refresh()
            sleep(0.15)

            self.menu[index]['Label'] = label
            self.draw()
            self.w.refresh()
            sleep(0.15)