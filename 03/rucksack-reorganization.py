# day 3: rucksack reorganization

priorities = [chr(i) for i in range(97, 123)]
priorities += [chr(i).upper() for i in range(97, 123)]

with open('input.txt', 'r') as f:
    ## variables
    # part one
    priority = 0

    # part two
    badges = []
    group = []
    ctr = 1

    for lines in f:
        row = lines.rstrip()
        group.append(set(row))

        if ctr < 3: ctr += 1
        else:
            # get the common item (ie. badge) in the elf group's rucksacks
            badge = (group[0].intersection(group[1])).intersection(group[2])
            badges.append(badge)

            group = []
            ctr = 1
        
        midpoint = int(len(row) / 2)
        first, second = [set(row[:midpoint]), set(row[midpoint:])]

        item = (first.intersection(second)).pop()

        priority += priorities.index(item) + 1

    print(priority)
    print(sum([priorities.index(b.pop()) + 1 for b in badges]))
