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
    max_cross = math.ceil(s*s/4)
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
        b5 = max(b5,0)
    if b4 > b3:
        b3 += 1
        b4 -= 1
        b4 = max(b4,0)
    if b3 > b2:
        b2 += 1
        b3 -= 1
        b3 = max(b3,0)
    print ('There will be the following ships:\n' + str(b5) + ' Carriers (5 fields long)\n' + str(b4) + ' Battleships (4 fields long)\n' + str(b3) + '  Cruisers (3 fields long)\n' + str(b2) + ' Destroyers (2 fields long)\n')
    set_boats_ranomly(5,b5,board1,s)
    set_boats_ranomly(4,b4,board1,s)
    set_boats_ranomly(3,b3,board1,s)
    set_boats_ranomly(2,b2,board1,s)
    print_board_owner(board1)
    set_boats_ranomly(5,b5,board2,s)
    set_boats_ranomly(4,b4,board2,s)
    set_boats_ranomly(3,b3,board2,s)
    set_boats_ranomly(2,b2,board2,s)
    print_board_owner(board2)

def set_boats_ranomly(len_boat, amnt_boats, board, size_board):
    for _ in range(amnt_boats):
        set_boat = False
        while not set_boat:
            row = randint(0,size_board-1)
            column = randint(0,size_board-1)
            direction = randint(0,1) # 0 means to the right, 1 means to the down
            if (direction == 0 and column+len_boat <= size_board) or (direction == 1 and row+len_boat <= size_board):
                # print (str(row) + ' - ' + str(column) + ' - ' + str(direction))
                setable = True
                for j in range(len_boat):
                    ### TO TEST
                    if j == 0:
                        if direction == 0 and (column-1 >= 0 and board[row][column-1] != 'O'):
                            setable = False
                            break
                        if direction == 1 and (row-1 >= 0 and board[row-1][column] != 'O'):
                            setable = False
                            break
                    if j == len_boat-1:
                        if direction == 0 and (column+j+1 < size_board and board[row][column+j+1] != 'O'):
                            setable = False
                            break
                        if direction == 1 and (row+j+1 < size_board and board[row+j+1][column] != 'O'):
                            setable = False
                            break
                    if direction == 0 and (board[row][column+j] != 'O' or (row-1 >= 0 and board[row-1][column+j] != 'O') or (row+1 < size_board and board[row][column+j] != 'O')):
                        setable = False
                        break
                    if direction == 1 and (board[row+j][column] != 'O' or (column-1 >= 0 and board[row+j][column-1] != 'O') or (column+1 < size_board and board[row+j][column+1] != 'O')):
                        setable = False
                        break
                if setable:
                    for j in range(len_boat,):
                        if direction == 0:
                            board[row][column+j] = 'V'
                        if direction == 1:
                            board[row+j][column] = 'V'
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

len_boat = 3 
amnt_boats = 1 
board = [['O','O','O','V','O'],['O','V','O','O','O'],['O','V','O','O','O'],['O','O','O','O','O'],['O','O','O','O','O']]

#OOOVO
#OVOOO
#OVOOO
#OOOOO
#OOOOO 22:20 - 

size_board = 5



setup_boards_auto()