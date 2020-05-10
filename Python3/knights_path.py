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
    origin_rank, origin_file = origin
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


def find_path(board, origin, destination, depth, path=[]):
    node = Tree(lookup_notation(board, origin))
    my_path = path[:]
    my_path.append(origin)
    if origin == destination:
        return Tree(lookup_notation(board, destination), True)
    if len(path) >= depth:
        node.children = False
        return node
    node.children = [find_path(board, hop, destination, depth, my_path)
                     for hop in valid_moves(board, origin) if hop not in my_path]
    return node


def main(origin, destination, depth=20):
    board = create_board()
    origin = lookup_coords(board, origin)
    destination = lookup_coords(board, destination)
    root = find_path(board, origin, destination, depth)
    # root.purge()
    return root


class Tree(object):
    def __init__(self, label, children=[]):
        self.label = label
        self.children = children

    def __repr__(self):
        return "%s -> %r" % (self.label, self.children)

    def paths(self, paths=[], path=[]):
        path.append(self.label)
        if self.children == True:
            paths.append(path)
            path = []
            return paths
        if self.children == False:
            path = []
            return paths
        return [child.paths(paths, path]) for child in self.children]
