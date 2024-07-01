from random import randint

# Creates an 6 x 6 board that will hold the player ships
player_board = [[' '] * 6 for x in range(6)]
# Creates an 6 x 6 board for player guesses
guess_board = [[' '] * 6 for x in range(6)]

# Converts letters to numbers
letters_to_numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5}


def print_board(board):
    print('  a b c d e f')
    print('-----------------')
    # Iterates 1 through to 6 and joins on a "|"
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


# Ships will be generated randomly
def make_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 5), randint(0, 5)
        while board[ship_row][ship_column] == 'x':
            ship_row, ship_column = randint(0, 5), randint(0, 5)
        board[ship_row][ship_column] = 'x'


# Will ask ther user the row and column for their guess
def ship_location():
    row = input('Enter a row number (1-6): ')
    # While loop if a number other than 1-6 is entered
    while row not in '123456':
        print('Error - please enter a number (1-6)')
        row = input('Enter a row number (1-6): ')
    column = input('Enter a column letter (a-f): ')
    # While loop if a letter other than a-f is entered
    while column not in 'abcdef':
        print('Error - please enter a letter (a-f)')
        column = input('Enter a column letter (a-f): ')
    return int(row) - 1, letters_to_numbers[column]


# Will count every time a ship is hit
def count_ships_hit(board):
    count = 0
    # For loop to increment score when a ship is hit
    for row in board:
        for column in row:
            if column == 'x':
                count += 1
    return count


make_ships(player_board)
# Determines the number of guesses
turns = 10
while turns > 0:
    print('Get ready to fire!')
    print("")
    print_board(guess_board)
    row, column = ship_location()
    # Will check to see if this guess has already been made
    if guess_board[row][column] == 'o':
        print("")
        print('Already guessed here - guess elsewhere.')
    # Places an x where a correct guess is made
    elif player_board[row][column] == 'x':
        print("")
        print('HIT!!!')
        guess_board[row][column] = 'x'
        # Counts down the number of turns remaining
        turns -= 1
    else:
        print("")
        print('** Miss - recalibrate your coordinates.**')
        # Add an '-' where the incorrect guess was made
        guess_board[row][column] = 'o'
        turns -= 1
    # Where all 5 computer ships have been hit
    if count_ships_hit(guess_board) == 5:
        print('You have successfully destroyed the enemy fleet!')
        break
    # Tells the user how many turns they have left
    print('You have ' + str(turns) + ' missles remaining.')
    print("")
    # Where all turns have been used up
    if turns == 0:
        print('You are out of missles - game over!')
        break
