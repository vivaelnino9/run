"""
Each boat is divided into section based on color for text. Each part of the boat has list of dicts each having 3 values:
    s: symbol used for the string
    y: head of boat y coordinate
    x: head of boat x coordinate
"""


def draw_small_sail(y, x):
    boat = {'main': [], 'sail': [], 'flag': []}
    # y - 0 (bottom)
    boat['main'].append({'s': '\\', 'y': y, 'x': x})
    for i in range(1, 10):
        boat['main'].append({'s': '_', 'y': y, 'x': x+i})
    boat['main'].append({'s': '/', 'y': y, 'x': x+9})
    # y - 1
    for i in range(1, 5):
        boat['main'].append({'s': '_', 'y': y-1, 'x': x+i})
    boat['main'].append({'s': '|', 'y': y-1, 'x': x+5})
    for i in range(6, 10):
        boat['main'].append({'s': '_', 'y': y-1, 'x': x+i})
    # y - 2
    boat['sail'] += [{'s': '//', 'y': y-2, 'x': x+3}, {'s': '_', 'y': y-2, 'x': x+4}, {'s': '|', 'y': y-2, 'x': x+5}]
    # y - 3
    boat['sail'] += [{'s': '/', 'y': y-3, 'x': x+4}, {'s': '|', 'y': y-3, 'x': x+5}]
    # y - 4
    boat['flag'] += [{'s': '~', 'y': y-4, 'x': x+4}, {'s': '.', 'y': y-4, 'x': x+5}]
    return boat


def draw_big_sail(y, x):
    boat = {'main': [], 'sail': [], 'top_sail': [], 'flag': []}
    # y - 0 (bottom)
    boat['main'].append({'s': '\\', 'y': y, 'x': x+4})
    for i in range(5, 26):
        boat['main'].append({'s': '_', 'y': y, 'x': x+i})
    boat['main'].append({'s': '/', 'y': y, 'x': x+26})
    # y - 1
    boat['main'] += [{'s': '\\', 'y': y-1, 'x': x+3}, {'s': '_', 'y': y-1, 'x': x+4},
                     {'s': '_', 'y': y-1, 'x': x+27}, {'s': '/', 'y': y-1, 'x': x+28}]
    # y - 2
    for i in range(8):
        boat['main'].append({'s': '_', 'y': y-2, 'x': x+i})
    boat['main'].append({'s': '|', 'y': y-2, 'x': x+8})
    for i in range(9, 19):
        boat['main'].append({'s': '_', 'y': y-2, 'x': x+i})
    boat['main'].append({'s': '|', 'y': y-2, 'x': x+19})
    for i in range(20, 29):
        boat['main'].append({'s': '_', 'y': y-2, 'x': x+i})
    # y - 3
    boat['sail'].append({'s': '/', 'y': y-3, 'x': x+4})
    for i in range(5, 12):
        boat['sail'].append({'s': '_', 'y': y-3, 'x': x+i})
    boat['sail'].append({'s': '\\', 'y': y-3, 'x': x+12})
    boat['sail'].append({'s': '/', 'y': y-3, 'x': x+15})
    for i in range(16, 23):
        boat['sail'].append({'s': '_', 'y': y-3, 'x': x+i})
    boat['sail'].append({'s': '\\', 'y': y-3, 'x': x+23})
    # y - 4
    for i in range(5, 8):
        boat['sail'].append({'s': '_', 'y': y-4, 'x': x+i})
    boat['main'].append({'s': '|', 'y': y-4, 'x': x+8})
    for i in range(9, 12):
        boat['sail'].append({'s': '_', 'y': y-4, 'x': x+i})
    for i in range(16, 19):
        boat['sail'].append({'s': '_', 'y': y-4, 'x': x+i})
    boat['main'].append({'s': '|', 'y': y-4, 'x': x+19})
    for i in range(20, 23):
        boat['sail'].append({'s': '_', 'y': y-4, 'x': x+i})
    # y - 5
    boat['top_sail'] += [{'s': ')', 'y': y-5, 'x': x+7}, {'s': '_', 'y': y-5, 'x': x+8}, {'s': '(', 'y': y-5, 'x': x+9},
                     {'s': ')', 'y': y-5, 'x': x+18}, {'s': '_', 'y': y-5, 'x': x+19}, {'s': '(', 'y': y-5, 'x': x+20}]
    # y - 6
    boat['top_sail'] += [{'s': '_', 'y': y-6, 'x': x+7}, {'s': '_', 'y': y-6, 'x': x+9},
                         {'s': '_', 'y': y-6, 'x': x+18}, {'s': '_', 'y': y-6, 'x': x+20}]
    boat['main'] += [{'s': '|', 'y': y-6, 'x': x+8}, {'s': '|', 'y': y-6, 'x': x+19}]

    # y - 7 (top)
    boat['flag'] += [{'s': '~', 'y': y-7, 'x': x+7}, {'s': '.', 'y': y-7, 'x': x+8},
                     {'s': '~', 'y': y-7, 'x': x+18}, {'s': '.', 'y': y-7, 'x': x+19}]

    return boat
