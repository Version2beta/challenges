def make_grid(size):
    return [[(y * size + x, weight_stay(size, y * size + x), weight_go(size, y * size + x))
             for x in range(1, size + 1)]
            for y in range(size)]


def weight_stay(size, n):
    exits = calc_exits(size, n)
    return exits * 2


def weight_go(size, n):
    exits = calc_exits(size, n)
    return exits + 1


def calc_exits(size, n):
    if n <= size or n > (size - 1) * size:
        if n % size in [0, 1]:
            return 2
        else:
            return 3
    elif n % size in [0, 1]:
        return 3
    else:
        return 4


def find_squares(size):
    return [n * n for n in range(1, size + 1)]


def flatten(l):
    return [item for sublist in l for item in sublist]


def calc_denom_stay(grid):
    return sum([sw for (_, sw, _) in flatten(grid)])


def calc_denom_go(grid):
    return sum([gw for (_, _, gw) in flatten(grid)])


def make_probability_grid(grid, denom_stay, denom_go):
    return [
        (sw/denom_stay + gw/denom_go) / 2 for (_, sw, gw) in flatten(grid)
    ]


def main(size):
    grid = make_grid(size)
    square_rooms = find_squares(size)
    denom_stay = calc_denom_stay(grid)
    denom_go = calc_denom_go(grid)
    probability_grid = make_probability_grid(grid, denom_stay, denom_go)
    probability = round(sum([probability_grid[n - 1]
                             for n in square_rooms]), 12)
    return probability
