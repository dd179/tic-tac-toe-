# Created by Dogan Alp Akbas
import random

# Print the board
def display_board(board):
    print(board[7], ' | ', board[8], ' | ', board[9])
    print('-', ' | ', '-', ' | ', '-')
    print(board[4], ' | ', board[5], ' | ', board[6])
    print('-', ' | ', '-', ' | ', '-')
    print(board[1], ' | ', board[2], ' | ', board[3])
# Take in player input
def player_input():
    choice = 'WRONG'
    correct_range = False

    while choice.isdigit() == False or correct_range == False:
        choice = input("Choose a number (1-9): ")
        if choice.isdigit() == False:
            print("Sorry, You didn't enter an integer. Please try again")

        if choice.isdigit() == True:
            if int(choice) not in range(1, 10):
                print("Your choice is not in the correct range")

            else:
                correct_range = True


    return int(choice)

# Place their input on the board
def place_marker(board, marker,position):

     board[position]=marker

     return board
# Check if the game is won
def win_check(board, mark):

    win_situation=[mark,mark,mark]
    for i in range(1,len(board),3):
        my_list=board[i:i+3]
        if my_list == win_situation:

            return True

    for i in range(1,4):
        new_lst =[]
        for j in range(i,len(board),3):
            new_lst.append(board[j])
            if new_lst == win_situation:

                return True

    diagonal_list =[]
    for i in range(1,len(board),4):
        diagonal_list.append(board[i])
        if diagonal_list == win_situation:
            return True

    diagonal_list_2= []
    for i in range(3,len(board),2):
        diagonal_list_2.append(board[i])
        if diagonal_list_2 == win_situation:
            return True

    return False

# Decide which player goes first

def choose_first():
    x=random.randint(0,1)
    if x == 0:

        return 'player_1'
    else:
        return 'player_2'

# Check the space on the board

def space_check(board, position):
    return board[position] == ' '


# Check the board is full
def full_board_check(board):

    for i in range(1,len(board)):
        if space_check(board,i):
            return False
    return True

# Play again ?
def replay():

    play = input("Do you want to play again ? (Y/N) : ")
    if play == 'Y':
        return True
    elif play == 'N':
        return False








