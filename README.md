# Connect-4
## Purpose
### I created this program to challenge myself by creating a computer that can play versus a human. This was especially difficult because I needed to think deeply about how humans think through moves and encode that. This game is made for anyone interested in playing Connect 4, but it is specially made as a challenge for myself.
## Breakthrough Moment
### One “breakthrough moment” I had was when trying to create an identical board such that the computer could simulate each column as an option. I tried trying board1 = board, but this caused board to change whenever board1 changed, which was not the purpose. I was able to overcome this by using the copy() function. 
### board1 = [b.copy() for b in board]
## Data Abstraction
### The board 2-D list is constantly being changed and stored. This data is retrived to check if a draw occured, to check if one of the players won, or to create possibilities that the computer could play. 
#### def draw():
####    for a in board:
####        for i in a:
####            if i != '⚪':
####                pass
####            else:
####                return False
####    return True
### The abstracted data represents the game board. 
### It manages complexity as the game board is constantly refered to such as when placing chips in the board, finding who won, or printing the board. 
## Procedural abstration
### One example of procedural abstration is the function that checks if someone has won horizontally:
#### def horizontal(x, b):
####    for i in range(6):
####        for a in range(4):
####            if b[i][a] == x and b[i][a + 1] == x and b[i][a + 2] == x and b[i][a + 3] == x:
####                return True
### It uses selection because it returns true *if* the horizontal is true.
### It uses iteration by repeating this process for every space in the board.
### It uses sequencing through the order of the function, as it starts on the left first then the right .
### This manages complexity because this function is referenced after every turn through the win() function. Rather than explicitly writing the code, I just reference the win() function which in turn references the horizontal() function. 
