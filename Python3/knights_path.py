def create_board():
    board = [(f"{list('abcdefgh')[file]}{rank + 1}", (file, rank))
             for file in range(8) for rank in range(8)]
    invert_board = [(loc, square) for square, loc in board]
    return (dict(board), dict(invert_board))


def valid_moves(board, origin):
    patterns = [
        (1, 2),
        (2, 1),
        (2, -1),
        (1, -2),
        (-1, -2),
        (-2, -1),
        (-2, 1),
        (-1, 2)
    ]
    origin_file, origin_rank = origin
    all_moves = [
        (origin_file + file_offset, origin_rank + rank_offset) for file_offset, rank_offset in patterns
    ]
    _, invert = board
    return [move for move in all_moves if move in invert]


def lookup_coords(board, square):
    board, _ = board
    return board.get(square)


def lookup_notation(board, location):
    _, invert = board
    return invert.get(location)


def find_path(board, origin, destination, depth, paths=dict(), path=tuple()):
    path = path + tuple([lookup_notation(board, origin)])
    if origin == destination:
        paths[path] = True
        path = ()
    elif depth < len(path):
        path = ()
    else:
        hops = valid_moves(board, origin)
        for hop in hops:
            if lookup_notation(board, hop) not in path:
                paths = find_path(board, hop, destination, depth, paths, path)
    return paths


def shortest_path(root):
    return sorted(list(root), key=len)[0]


def main(origin, destination, depth=20):
    board = create_board()
    origin = lookup_coords(board, origin)
    destination = lookup_coords(board, destination)
    root = find_path(board, origin, destination, depth)
    return sorted(list(root), key=len)
