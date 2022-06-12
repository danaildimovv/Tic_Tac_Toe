import os


def display_board(board):       # creates the board
    print("\n" * 100)
    print("   |     |   ")
    print(board[7], " | ", board[8], " | ", board[9]," ")
    print("___|_____|___")
    print("   |     |   ")
    print(board[4], " | ", board[5], " | ", board[6]," ")
    print("___|_____|___")
    print("   |     |   ")
    print(board[1], " | ", board[2], " | ", board[3]," ")
    print("   |     |   ")


def player_input():        # takes players marker
    player1 = ""           # assigns an empty string for player 1 marker

    player1name = input("Hello, what is your name? ")

    while player1 != "X" and player1 != "x" and player1 != "O" and player1 != "o":            # while the input is different from X and O the console asks
        player1 = input(f"Hello, {player1name}. Please choose X or O: ")     # the console wants an input from player 1
        print(f"So, {player1name}, you will play with {player1.upper()}")

        player2name = input("Hello, what is your name?")

    if player1 == "x" or player1 == "X":          # if player 1 chooses X,
        player2 = "O"           # then player 2 is O

    else:                       # else
        player2 = "X"           # player 2 is X

    print(f"Hello, {player2name}. You will play with {player2}.")

    return player1, player2, player1name, player2name     # returns a tuple with player 1 and player 2 markers


def placement(place, data, marker, player):                     # a function to put the player's marker on its place
    place = int(input(f"Where do you wanna play, {player}? "))     # asks the player for a number of position

    while data[place] == "X" or data[place] == "O" or data[place] == "o" or data[place] == "x":
        place = int(input("It is not okay to put it there. Where? "))

    data[place] = marker                                # places the marker on the chosen place


def winner(board):
    if (board[1] == board[2] == board[3]) or (board[4] == board[5] == board[6]) or (board[7] == board[8] == board[9]) or (board[1] == board[4] == board[7]) or (board[3] == board[6] == board[9]) or (board[2] == board[5] == board[8]) or (board[1] == board[5] == board[9]) or (board[3] == board[5] == board[7]):
        return True
    return False


print("Welcome to Tic-Tac-Toe")                         # prints a welcome message

choice = input("If you feel ready to start the game type 'Yes'. Otherwise type anything you want. ")

#                                         ^
# asks the player if he/she wants to play |
#                                         |


players_info = ()       # creates an empty tuple for players' markers (used later)

if choice.lower() == "yes":                             # if the player wants to play
    players_info = player_input()                       # assigns players' markers to players_info
    os.system("cls")

    player1_marker = players_info[0]                    # stores player 1 marker in the variable player1_marker
    player2_marker = players_info[1]                    # stores player 2 marker in the variable player2_marker
    player1_name = players_info[2]
    player2_name = players_info[3]

    choices = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # a list, which stores players' choices of place

    player1_choice = 0
    player2_choice = 0

    while not winner(choices):

        display_board(choices)                                              # calling the function display_board(board)

        placement(player1_choice, choices, player1_marker, player1_name)
        display_board(choices)

        winner(choices)

        if not winner(choices):
            placement(player2_choice, choices, player2_marker, player2_name)
            display_board(choices)

            winner(choices)

    counterX = 0
    counterO = 0
    for sign in choices:
        if sign == "X":
            counterX += 1
        elif sign == "O":
            counterO +=1

    if counterX == 3:
        if player1_marker == "X":
            print("Congratulations, Player 1! You win!")
        elif player2_marker == "X":
            print("Congratulations, Player 2! You win!")

    elif counterO == 3:
        if player1_marker == "O":
            print("Congratulations, Player 1! You win!")
        elif player2_marker == "O":
            print("Congratulations, Player 2! You win!")

else:
    print("You can leave.")
    quit()