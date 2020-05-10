#!/usr/bin/env python3

import random
squares = 0
visits = 0


def workspace(x, y):
    return [[(False, False) for _ in range(y)] for r in range(x)]


def add_queen(workspace, x, y):
    global visits
    working = [d[:] for d in workspace]
    (_, attacked) = working[x][y]
    if attacked:
        return (False, workspace)
    rows, cols = (range(len(working)), range(len(working[0])))
    for row in rows:
        for col in cols:
            visits = visits + 1
            if row == x or col == y or abs(row - x) == abs(col - y):
                (queen, _attacked) = working[row][col]
                if queen:
                    return (False, workspace)
                working[row][col] = (row == x and col == y,
                                     not (row == x and col == y) or attacked)
    return (True, working)


def add_queens(board, numqueens):
    global squares
    if numqueens == 0:
        return (True, board)
    rows, cols = (list(range(len(board))), list(range(len(board[0]))))
    random.shuffle(rows)
    random.shuffle(cols)
    for row in rows:
        for col in cols:
            squares = squares + 1
            working = [d[:] for d in board]
            valid_one, working = add_queen(working, row, col)
            if valid_one:
                valid_all, working = add_queens(working, numqueens - 1)
                if valid_all:
                    return (True, working)
    return (False, board)


def render(workspace):
    return [["Q" if queen else "X" if attacked else "." for queen, attacked in row] for row in workspace]


def from_workspace(workspace):
    return [[1 if queen else 0 for queen, _attacked in row] for row in workspace]


def main(x, y, numqueens):
    global squares, visits
    squares, visits = (0, 0)
    initial_board = workspace(x, y)
    valid, solution = add_queens(initial_board, numqueens)
    print(visits, "visits to", squares, "squares")
    for rank in render(solution):
        print(rank)
    if valid:
        return from_workspace(solution)
    else:
        return []
