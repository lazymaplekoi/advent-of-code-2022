# day 5: supply stacks
import re

def parse_stacks(stack, rows):
    for row in rows:
        stack_num = 1
        i = 0
        while i < len(row):
            crate = re.sub(r'\W', '', row[i])
            if crate == '':
                i += 4
            else:
                stack[stack_num] = [crate] + stack[stack_num]
                i += 1
            
            stack_num += 1

def move_crates(stack, moves):
    for count, src, dest in moves:
        # sanity check if source stack has enough crates to move
        if not len(stack[src]) or count > len(stack[src]):
            continue
        
        # for i in range(count):                # retaining as comment for part 2
        if count == 1:
            # mechanism used for part 1
            stack[dest].append(stack[src].pop())
            continue
        
        n = len(stack[src]) - count
        
        stack[dest] += stack[src][n:]
        stack[src] = stack[src][:n]

def stack_tops(stack):
    stacks = stack.values()
    return ''.join([s[-1] for s in stacks])

with open('input.txt', 'r') as f:
    init_stack = []
    stack_count = 0
    stack = {}
    moves = []

    # flag for reading input
    read_stack = True

    # read input
    for lines in f:
        line = lines.rstrip('\n')
        if (line == ''): read_stack = False

        if read_stack:
            line = line.split(' ')
            init_stack.append(line)
            continue
        
        # get moves list after stack data
        move = re.findall(r'\d+', line)
        if len(move): moves.append([int(m) for m in move])
        
    # get number of stacks
    stack_base = (list(filter(None, init_stack.pop())))
    stack_count = len(stack_base)

    # initialize stack
    stack = { i : [] for i in range(1, stack_count+1) }
    parse_stacks(stack, init_stack)

    # start moving crates
    move_crates(stack, moves)
    print(stack)

    print(stack_tops(stack))