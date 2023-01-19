import sys
import os
import random

#board

board = []
for i in range(6):
    row = []
    for a in range(7):
        row.append('⚪')
    board.append(row)

def print_board():
    os.system('clear')
    # print each circle, with a line in between each to appear like a board, and a new line for every row
    for i in range(6):
        for a in range(7):
            print("|", end="")
            print(board[i][a], end="")
        print("|", end="")
        print()
    print(" ", end="")
    for i in range(7):
        print(i + 1, " ", end="")
    print()

# win

#checking if won horizontally
def horizontal(x, b):
    for i in range(6):
        for a in range(4):
            if b[i][a] == x and b[i][a + 1] == x and b[i][a + 2] == x and b[i][a + 3] == x:
                return True

#checking if won vertically
def vertical(x, b):
    for i in range(3):
        for a in range(7):
            if b[i][a] == x and b[i + 1][a] == x and b[i + 2][a] == x and b[i + 3][a] == x:
                return True

#checking if won diagonally (top left to bottom right)
def diagonal1(x, b):
    for i in range(3):
        for a in range(4):
            if b[i][a] == x and b[i + 1][a + 1] == x and b[i + 2][a + 2] == x and b[i + 3][a + 3] == x:
                return True

#checking if won diagonally (top right to bottom left)
def diagonal2(x, b):
    for i in range(3):
        for a in range(4):
            if b[5 - i][a] == x and b[4 - i][a + 1] == x and b[3 - i][a + 2] == x and b[2 - i][a + 3] == x:
                return True


def win(b):
    if horizontal('🟡', b) == True:
        return "yellow"
    if horizontal('🔴', b) == True:
        return "red"

    if vertical('🟡', b) == True:
        return "yellow"
    if vertical('🔴', b) == True:
        return "red"

    if diagonal1('🟡', b) == True:
        return "yellow"
    if diagonal1('🔴', b) == True:
        return "red"

    if diagonal2('🟡', b) == True:
        return "yellow"
    if diagonal2('🔴', b) == True:
        return "red"

# if no empty places, draw

def draw():
    for a in board:
        for i in a:
            if i != '⚪':
                pass
            else:
                return False
    return True

# prompting user

# prompt for playing versus computer or friend
def prompt():
    os.system('clear')
    choice = input("computer (1) or friend (2)? ")
    if choice != '1' and choice != '2':
        prompt()
    return choice

# prompt for entering column
def column():
    c = input("column: ")
    try:
        c = int(c) - 1
    except ValueError:
        # returning 9 will cause the function to re-run
        return 9
    return c

#entering a chip in a board
def chip(color, column, b):
    if color == "yellow":
        for i in range(6):
            if b[5 - i][column] == '⚪':
                b[5 - i][column] = '🟡'
                return
    if color == "red":
        for i in range(6):
            if b[5 - i][column] == '⚪':
                b[5 - i][column] = '🔴'
                return

# to be referenced in computer choice

# checks if a player will win based on a given choice
def willwin(a, color, b):
    chip(color, a, b)
    if win(b) == "red":
        return "red"
    if win(b) == "yellow":
        return "yellow"
    return None

# other possibilites if no winning option
def possibilities():
    pos = [0, 1, 2, 3, 4, 5, 6]
    # remove option if column is full
    for number in pos:
        if board[0][number] != '⚪':
            pos.remove(number)
    pos1 = pos.copy()

    for number in pos:
        # doesn't place a chip that would allow the opponent to win
        board1 = [b.copy() for b in board]
        chip("red", number, board1)
        chip("yellow", number, board1)
        if willwin(a, "yellow", board1):
            pos.remove(number)
        # doesn't place a chip that would allow the opponent to block
        chip("yellow", number, board1)
        chip("red", number, board1)
        if willwin(a, "red", board1) and number in pos:
            pos.remove(number)
    if pos != []:
        return random.choice(pos)
    else:
        # if no good choices, chooses one at random from those avaliable
        return random.choice(pos1)


def computer():
    # if will win from an option, play
    for a in range(7):
        board1 = [b.copy() for b in board]
        if willwin(a, "red", board1) == "red":
            return a

    # if opponent will win from an option, block
    for a in range(7):
        board1 = [b.copy() for b in board]
        if willwin(a, "yellow", board1) == "yellow":
            return a

    return possibilities()


def main():
    choice = prompt()
    # versus friend
    if choice == '2':
        for i in range(22):
            print_board()

            if win(board) == 'red':
                print("Red wins!")
                return
            if draw() == True:
                print_board()
                print("Draw!")
                return

            # player 1 (yellow)
            print("Player 1 (yellow)")

            c = column()
            while c < 0 or c > 6:
                print("column out of range")
                print("re-enter column")
                c = column()

            while board[0][c] != '⚪':
                print("column is full")
                print("re-enter column")
                c = column()

            chip("yellow", c, board)
            print_board()

            if win(board) == 'yellow':
                print("Yellow wins!")
                return
            if draw() == True:
                print_board()
                print("Draw!")
                return

            # player 2 (red)
            print("Player 2 (red)")

            c = column()
            while c < 0 or c > 6:
                print("column out of range")
                print("re-enter column")
                c = column()

            chip("red", c, board)

    # versus computer
    if choice == '1':
        # first row
        # player (yellow)
        print_board()
        print("Player (yellow)")

        c = column()
        while c < 0 or c > 6:
            print("column out of range")
            print("re-enter column")
            c = column()

        while board[0][c] != '⚪':
            print("column is full")
            print("re-enter column")
            c = column()

        chip("yellow", c, board)
        print_board()

        if win(board) == 'yellow':
            print("Player (yellow) wins!")
            return
        if draw() == True:
            print_board()
            print("Draw!")
            return

        # computer (red)
        if board[5][3] == '⚪':
            c = 3
        else:
            c = 4
        chip("red", c, board)

        for i in range(22):
            print_board()

            if win(board) == 'red':
                print("Computer (red) wins!")
                return
            if draw() == True:
                print_board()
                print("Draw!")
                return

            # player (yellow)
            print("Player (yellow)")

            c = column()
            while c < 0 or c > 6:
                print("column out of range")
                print("re-enter column")
                c = column()

            while board[0][c] != '⚪':
                print("column is full")
                print("re-enter column")
                c = column()

            chip("yellow", c, board)
            print_board()

            if win(board) == 'yellow':
                print("Player (yellow) wins!")
                return
            # draw
            if draw() == True:
                print_board()
                print("Draw!")
                return

            # computer (red)
            c = computer()
            chip("red", c, board)


if __name__ == "__main__":
    main()