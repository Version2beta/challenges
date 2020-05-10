singles = list(range(1, 21)) + [25]
doubles = singles[:]
trebles = doubles[:-1]
regions = [
    (f"S{n}", n) for n in singles
] + [
    (f"D{n}", n * 2) for n in doubles
] + [
    (f"T{n}", n * 3) for n in trebles
]
doubles_regions = [(f"D{n}", n * 2) for n in doubles]

all_combinations = [
    [rd] for rd in doubles_regions
] + [
    [r, rd] for r in regions for rd in doubles_regions
] + [
    [r1, r2, rd] for r1 in regions for r2 in regions for rd in doubles_regions
]

combinations = []
seen = []
for e in all_combinations:
    if len(e) < 3:
        combinations.append(e)
    elif e[1][0] == e[0][0]:
        combinations.append(e)
    elif (e[1][0], e[0][0]) not in seen:
        combinations.append(e)
        seen.append((e[0][0], e[1][0]))


# def filter_fn(combination):
#     return sum([points for _region, points in combination]) == 6


def filter_fn(combination):
    return sum([points for _region, points in combination]) < 100
