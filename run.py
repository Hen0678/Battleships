from random import randint

# Creates an 8 x 8 board that will hold the player ships
player_board = [[' '] * 8 for x in range(8)]
# Creates an 8 x 8 board for player guesses
guess_board = [[' '] * 8 for x in range(8)]
print(player_board)
print(guess_board)

# A way to convert letters to numbers
letters_to_numbers = {'a': 0, 'b': 1, 'c':2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}

def print_board(board):
    print('a b c d e f g h')
    print('---------------')
    # Iterates 1 through to 8 and joins on a "|" 
    row_number = 1
    for row in board:
        print("%d|%s|" %  (row_number, "|".join(row)))
        row_number += 1

# Ships will be generated randomly 
def make_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,7), randint(0,7)
        while board[ship_row][ship_column] == 'x':
            ship_row, ship_column = randint(0,7), randint(0,7)
        board[ship_row][ship_column] = 'x'

# Will ask ther user the row and column for their guess
def ship_location():
    row = input('Enter a row number (1-8)')
    # While loop if a number other than 1-8 is entered
    while row not in '12345678':
        print('Error - please enter a number (1-8)')
        row = input('Enter a row number (1-8)')
    column = input('Enter a column letter (a-h)')
    while column not in 'abcdefgh':
        print('Error - please enter a letter (a-h)')
        column = input('Enter a column letter (a-h)')
    return int(row) - 1, letters_to_numbers[column]





# Will count every time a ship is hit
def count_ships_hit():
    pass

