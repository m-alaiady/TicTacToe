import math
import random
import os

# game board
game = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# play with Computer or 2 players
game_mode = 0
# current player x by default
current_player = "x"
# get current position
position = -1
# check if its computer turn
computer_turn = False
# check if it is draw by counting each turns
turn_steps = 0


# clear console for both windows and linux OS
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)


# display the game board
def board():
    counter = 1
    clearConsole()
    print('-------------')
    for row in game:
       for item in row:
           print(f"| {item} ", end="")
           if counter % 3 == 0:
               print("|", end="")
           counter = counter + 1
       print("")

    counter = 0
    print('-------------')


# check if given input is numeric
def is_num(num):
    if not num.isnumeric():
        return False
    else:
        return True


# check if given input is in right range(1 - 9)
def is_in_range(num):
    if 1 <= int(num) <= 9:
        return True
    else:
        return False


# check if a place is already taken by another player
def is_taken(row, col):
    if game[row][col] == "x" or game[row][col] == "o":
        return True
    else:
        return False


def check_if_draw():
    if turn_steps >= 8:
        return True
    else:
        return False


# check if any players win
def check_if_win(row):
    win = False
    if check_row(row) or check_column() or check_diagonal():
        win = True
    return win


# check if a player win by row
def check_row(row):
    win_row = True
    for pos in game[row]:
        if pos != current_player:
            win_row = False
            break
    return win_row


# check if a player win by column
def check_column():
    for i in range(3):
        win_column = True
        for j in range(3):
            if game[j][i] != current_player:
                win_column = False
                break
        if win_column:
            return True
    return False


# check if a player win by diagonal
def check_diagonal():
    if game[0][0] == current_player and game[1][1] == current_player and game[2][2] == current_player:
        return True
    elif game[0][2] == current_player and game[1][1] == current_player and game[2][0] == current_player:
        return True
    else:
        return False


# if X turn finished then go to O turn
def switch_player():
    global current_player

    if current_player == "x":
       current_player = "o"
    elif current_player == "o":
        current_player = "x"


def computer_player():
    while True:
        temp = random.randint(1,9)
        row = int((int(temp) - 1) / 3)
        col = int((int(temp) - 1) % 3)
        if not is_taken(row, col):
            return str(temp)
            break


def get_position():
    global position, computer_turn

    if game_mode == "1":
        position = computer_player()
        computer_turn = False
    elif game_mode == "2":
        position = input("Choice number: ")


def game_mode():
    # 1 for computer , 2 for 2 players
    global game_mode
    game_mode = input("Enter your player mode:\n\n1 - play with Computer\n2 - play with 2 Players\n> ")

    # computer mode
    if game_mode == "1":
        print("Computer Mode Selected")
    elif game_mode == "2":
        print("2 Players Mode Selected")
    else:
        print("Invalid choice, select either 1 or 2")


def tic_tac_toe():
    global computer_turn, position, turn_steps
    game_mode()
    while True:
        board()
        if computer_turn:
            get_position()
        else:
            position = input("Choice number: ")
            computer_turn = True

        if is_num(position) and is_in_range(position):
            row = int((int(position) - 1) / 3)
            col = int((int(position) - 1) % 3)

            if not is_taken(row, col):
                game[row][col] = current_player
                if check_if_win(row):
                    board()
                    print(f"{current_player} Winned!")
                    break
                elif check_if_draw():
                    board()
                    print(f"Draw ")
                    break
                else:
                    switch_player()
                    turn_steps = turn_steps + 1
            else:
                print('position is taken, choose another')
                continue
        else:
            print('Invalid choice, Enter from 1 to 9')
            continue


tic_tac_toe()
