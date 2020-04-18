import random
import time

def display_board(board):
    """ Display a 3 by 3 board """
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('–' * 11)
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('–' * 11)
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def player_input():
    """ Players marker selectiion, 'X' or 'O' """
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Pick a marker 'X' or 'O': ").upper()

    if marker == 'O':
        return ('O', 'X')

    return ('X', 'O')

def place_marker(board, marker, position):
    """ Places player input on the board"""
    board[position] = marker
    return board

def choose_first():
    """ Randomly selects which player goes first"""
    i = random.randint(0,1)
    print(f'\nPlayer {i+1} goes first. May the Odds be in your Favor!!!')

def space_check(board, position):
    """ Check board for empty space on board"""
    return board[position] == ' '

def full_board_check(board):
    """ check to see if the board is filled"""
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    """Input request for user to select a position on the board """
    position = int(input('Please enter next position (as a number 1-9): '))
    while not space_check(board, position):
        position = int(input('Please re-enter next position (1-9), initial position already occupied: '))
    return position

def win_check(board, mark):
    """checks for the winner on the board"""
    return((board[1]==board[2]==board[3]==mark)|
           (board[4]==board[5]==board[6]==mark)|
           (board[7]==board[8]==board[9]==mark)|
           (board[1]==board[4]==board[7]==mark)|
           (board[8]==board[5]==board[2]==mark)|
           (board[9]==board[6]==board[3]==mark)|
           (board[1]==board[5]==board[9]==mark)|
           (board[3]==board[5]==board[7]==mark))

def replay():
    return input('Do you want to replay my TicTac game ("Yes" or "No"): ').lower().startswith('y')

def tic_tac_toe():
    """ Boady of the game using all function from above"""
    while True:
        print('\nIt is about to get real !!!.\nPlease take a look at the layout of the board.\nThe numbers represents where your markers will sit')
        time.sleep(6)
        template = ['#', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        display_board(template)
        time.sleep(6)
        print('Now that you are all caught on, let have some fun...')
        main_board = [' '] * 10
        main_board[0] = '$'
        display_board(main_board)

        print('\nWho should go first, Thinking.....')
        time.sleep(3)
        choose_first()
        print('\n')
        player_1, player_2 = player_input()
        ready = input('\nAre you ready to play ("Yes" or "No"): ')

        if ready[0].lower() == 'y':
            game_on = True
        else:
            game_on = False
        counter = 0

        while game_on:
            print('\n')
            position = player_choice(main_board)
            place_marker(main_board, player_1, position)
            display_board(main_board)
            counter += 1
            if counter >= 3:
                if win_check(main_board, player_1):
                    print(f'\nPlayer with marker "{player_1}" won !!!')
                    break
                elif (counter >= 8) & (full_board_check(main_board)):
                    print(f'\nThis round is a draw... Try again\n')
                    break

            # Player2's turn
            print('\n')
            print('Next Player Please')
            print('\n')
            position = player_choice(main_board)
            place_marker(main_board, player_2, position)
            display_board(main_board)
            counter += 1
            if counter >= 3:
                if win_check(main_board, player_2):
                    print(f'Player with marker "{player_2}" won !!!')
                    print('\n')
                    break

                elif (counter >= 8) & (full_board_check(main_board)):
                    print(f'Board is full and no winner emerged')
                    print('\n')
                    break
            print('\n ')
            print('Next Player Please')
            print('\n')

        if not replay():
            print('\n\nwe will miss you, see you soon')
            break

def main():
    print('\nWelcome to the Xs and Os, aka TicTacToe !!!')
    time.sleep(3)
    print('\nLoading....')
    time.sleep(3)
    tic_tac_toe()

if __name__ == '__main__':
    main()
