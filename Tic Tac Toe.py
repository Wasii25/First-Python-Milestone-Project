import random
#TO DISPLAY THE BOARD
def display_board(board):

    print(" ___________ ")
    print("| " + board[7] + " | " + board[8] + " | " + board[9] + " |")
    print("|-----------|")
    print("| " + board[4] + " | " + board[5] + " | " + board[6] + " |")
    print("|-----------|")
    print("| " + board[1] + " | " + board[2] + " | " + board[3] + " |")
    print(" -----------")

#TO TAKE IN PLAYER INPUT
def player_input():
    p1, p2 = '', ''

    while p1 not in ['X', 'O']:
        p1 = input("Player 1: choose your option X or O: ")

        if p1 not in ['X', 'O']:
            p1 = input("I'm sorry. I don't understand. Please choose between X and O only")

    if p1 == 'X':
        p2 = 'O'
    else:
        p2 = 'X'
    return p1, p2

#A FUNCTION THAT TAKES A BOARD LIST AS AN OBJECT, A MARKER ('X' OR 'O') AND A DESIRED POSITION NUMBER (1-9) AND ASSIGNS IT TO THE BOARD
def place_marker(board, marker, position):
    board[position] = marker

#A FUNCTION TO TAKE IN A BOARD, A MARK(X OR O) AND CHECKS TO SEE IF THE MARK HAS WON
def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[1] == board[2] == board[3] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark))

    #A FUNCTION TO RANDOMLY DECIDE WHICH PLAYER GOES IN FIRST
def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'

#A FUNCTION TO CHECK IF THE GIVEN SPACE ON THE BOARD IS FREELY AVAILABLE (RETURN A BOOLEAN)
def space_check(board, position):
    return board[position] == ' '

#A FUNCTION TO CHECK IF THE BOARD IS FULL AND RETURNS A BOOLEAN VALUE
def full_board_check(board):
    for i in board:
        if i == ' ':
            return False
    return True

#A FUNCTION THAT ASKS FOR A PLAYER'S NEXT POSITION AS A NUMBER(1-9) AND THEN CHECK IF IT'S A FREE POSITION, IF YES RETURN THE POSITION:
def player_choice(board):
    n = 0
    while n not in range(0, 10) or not space_check(board, n):
        n = int(input("Choose your next position (0-9): "))
    return n

#A FUNCTION TO ASK THE PLAYERS IF THEY WANNA PLAY AGAIN
def replay():
    o = ' '
    while o not in ['Y', 'N', 'y', 'n']:
        o = input("Do you wanna play again?? Choose y or n")

        if o.lower() == 'y':
            return True
        elif o.lower() == 'n':
            return False
        else:
            print("I'm sorry. I don't understand. Please choose between y or n only")

#THE GAME FINALLY!!!
print("Welcome to Tic Tac Toe")

while True:
    board = [' ']*10
    turn = choose_first()
    print(turn + " will go first")
    p1,p2 = player_input()
    play_game = input("Are you ready to play??? Y or N: ")

    if play_game.lower() == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            display_board(board)
            pos = player_choice(board)
            place_marker(board, p1, pos)

            if win_check(board, p1) == True:
                display_board(board)
                print("Player 1 wins the game!!!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a draw!!")
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            pos = player_choice(board)
            place_marker(board, p2, pos)

            if win_check(board, p2) == True:
                display_board(board)
                print("Player 2 wins the game!!!")
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("It's a draw!!")
                else:
                    turn = 'Player 1'

    if not replay():
        break
