# day 4: camp cleanup

def parse(row: list) -> tuple:
    first = row[0].split('-')
    first_range = range(int(first[0]), int(first[1])+1)

    second = row[1].split('-')
    second_range = range(int(second[0]), int(second[1])+1)

    return (set(first_range), set(second_range))

def contains(range1, range2) -> bool:
    return range1.issubset(range2) or range2.issubset(range1)

def overlaps(range1, range2) -> bool:
    return len(range1.intersection(range2))

with open('input.txt', 'r') as f:
    fully_contains = 0
    overlap = 0

    for sections in f:
        row = sections.rstrip().split(',')
        section1, section2 = parse(row)
        if contains(section1, section2): fully_contains += 1
        if overlaps(section1, section2): overlap += 1

    print(fully_contains)
    print(overlap)