import math


def gen_mountain(start, end, base_height):
    slope = math.ceil((end - start) / 2)

    y_list = list(range(base_height, base_height - slope, -1)) + list(range(base_height - slope + 1, base_height + 1))
    x_list = range(start, end+1)
    symbols = ['/'] * slope + ['\\'] * slope

    return list(zip(y_list, x_list, symbols))


if __name__ == '__main__':
    print(gen_mountain(5, 10, 11))