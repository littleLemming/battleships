from random import randint
import sys
import math

"""
method that takes a string as an argument
it prints the string and then cleanly exits the program 
this method will be called if an error occurs that can't be handled (exception, wrong user intput,...)
"""
def bail_out(s):
    print(s)
    sys.exit()

"""
this method sets up 2 boards automatically
one vlaue will be asked from the player:
s is the size of the board (sxs)
there will be large and small boats - the larges boat can be s-2 or 5 (whichever is smaller)
both boards will have the same amount of boats of the same size
"""
def setup_boards_auto():
    s = int(input("Enter the size of the two boards (at least 4, no more than 20): "))
    if s < 4:
        bail_out("The size of the board needs to be at least 4!")
    if s > 20:
        bail_out("The size of the board can't be larger than 20!")
    max_len = min(5,s-2)
    board1 = []
    board2 = []
    for i in range(s):
        board1.append(["O" for i in range(s)])
        board2.append(["O" for i in range(s)])
    max_cross = math.ceil(s*s/3)
    print('The size of the longest ship will be: ' + str(max_len))
    b5, b4, b3 = 0, 0, 0
    if max_len >= 5:
        b5 = math.ceil(max_cross/5/3)
        max_cross -= b5*5
    if max_len >= 4:
        b4 = math.ceil(max_cross/4/3)
        max_cross -= b4*4
    if max_len >= 3:
        b3 = math.ceil(max_cross/3/3) + 1
        max_cross -= b3*3-3
    b2 = math.ceil(max_cross/2/3) + 2
    if b5 >= b4:
        b4 += 1
        b2 += 1
        b5 -= 1
    if b4 > b3:
        b3 += 1
        b4 -= 1
    if b3 > b2:
        b2 += 1
        b3 -= 1
    print ('There will be the following ships:\n' + str(b5) + ' Carriers (5 fields long)\n' + str(b4) + ' Battleships (4 fields long)\n' + str(b3) + '  Cruisers (3 fields long)\n' + str(b2) + ' Destroyers (2 fields long)\n')
    set_boats_ranomly(5,b5,board1,s)
    set_boats_ranomly(4,b4,board1,s)
    print_board_owner(board1)
    print_board_owner(board2)

def set_boats_ranomly(len_boat, amnt_boats, board, size_board):
    for _ in range(amnt_boats):
        set_boat = False
        for _ in range(10):
            row = randint(0,size_board-1)
            column = randint(0,size_board-1)
            direction = randint(0,3) # 0 means to the right, 1 means to the left, 2 means up, 3 means down
            if (direction == 0 and row+len_boat < size_board) or (direction == 1 and row-len_boat >= 0) or (direction == 2 and column-len_boat >= 0) or (direction == 3 and column+len_boat < size_board):
                print(str(row) + ' - ' + str(column) + ' - ' + str(direction))
                setable = True
                for j in range(len_boat,):
                    if not ((direction == 0 and board[row+j][column] == 'O') or (direction == 1 and board[row-j][column] == 'O') or (direction == 2 and board[row][column-j] == 'O') or (direction == 3 and board[row][column+j] == 'O')):
                        # TODO missing rule about not setting directly next to each other
                        setable = False
                        break
                if setable:
                    for j in range(len_boat,):
                        if direction == 0:
                            board[row+j][column] = 'V'
                        if direction == 1:
                            board[row-j][column] = 'V'
                        if direction == 2:
                            board[row][column-j] = 'V'
                        if direction == 3:
                            board[row][column+j] = 'V'
                    set_boat = True 
            if set_boat:
                break         
        if not set_boat:
            bail_out("Within 10000 a ship could not be placed. Therefor the program gets terminated.")

"""
this method lets the players set up their boars
two values will be asked from the player before they can place their battleships:
s is the size of the board (sxs)
b is the amount of battleships there will be
b can't be larger than s
afterwards they will have to enter their battleships (they will have different sizes)
"""
def setup_boards():
    print("NOT YET IMPLEMENTED")

""" 
this methods prints the board for the owner
O marks an empty spot
X marks an already sunken boat
V marks a boat that has not yet sunken
"""
def print_board_owner(board):
    for i in board:
        print(' '.join(i))
    print('\n')

def print_board_opponent():
    print("NOT YET IMPLEMENTED")


setup_boards_auto()