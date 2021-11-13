# Play Rock Paper Scissor

import random


def play():
    user = input("What's Your Choice?\nPick 'r' for Rock, 'p' for Paper and 's' for Scissor ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'It\'s a Tie'

    if won(user, computer):
        return 'You Won!'

    return 'You Lost :('



# r>s, s>p, p>r
def won(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True


print(play())
