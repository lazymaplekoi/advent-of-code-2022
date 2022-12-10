### day 2: rock paper scissors

scoreboard = {
    'A' : { 'X' : 3, 'Y': 6, 'Z': 0 },
    'B' : { 'X' : 0, 'Y': 3, 'Z': 6 },
    'C' : { 'X' : 6, 'Y': 0, 'Z': 3 }
}

outcomes = {'X' : 0, 'Y' : 3, 'Z' : 6}
choices = list(outcomes.keys())

def calculate_score(opponent, you):
    return scoreboard[opponent][you] + choices.index(you) + 1

def calculate_score_two(opponent, outcome):
    score = outcomes[outcome]
    # get index of score in opponent's move matrix
    you = [move for move, s in scoreboard[opponent].items() if s == score][0]
    return score + choices.index(you) + 1

if __name__ == '__main__':
    with open('input.txt', 'r') as f:
        total = 0
        total_two = 0
        for lines in f:
            [opponent, you] = lines.rstrip().split()
            
            # part one: second column denotes your move
            # (X - rock, Y - paper, Z - scissors)
            total += calculate_score(opponent, you)

            # part two: second column denotes the outcome of the round
            # (X - lose, Y - draw, Z - win) 
            total_two += calculate_score_two(opponent, you)


        print(total)
        print(total_two)
