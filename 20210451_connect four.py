
rows = 6
columns = 7


def construct_board(rows, columns):
    board = [['.' for c in range(columns)] for r in range(rows)]
    return board


def display_board(board):
    for row in board:
        for column in row:
            print(column, end=' ')
        print()
    return board


def insert_at(board, c, indx, rows):
    for row in range(-1, (rows + 1) * -1, -1):
        if board[row][indx - 1] == '.':
            board[row][indx - 1] = c
            return True
    return False


def winning_move(board, pos):
    # Check horizontal locations for win
    for c in range(columns - 4):
        for r in range(rows):
            if board[r][c] == pos and board[r][c + 1] == pos and board[r][c + 2] == pos and board[r][c + 3] == pos:
                return True

    # Check vertical locations for win
    for c in range(columns):
        for r in range(rows - 3):
            if board[r][c] == pos and board[r + 1][c] == pos and board[r + 2][c] == pos and board[r + 3][c] == pos:
                return True

    # Check positively sloped diaganols
    for c in range(columns - 3):
        for r in range(rows - 3):
            if board[r][c] == pos and board[r + 1][c + 1] == pos and board[r + 2][c + 2] == pos and board[r + 3][c + 3] == pos:
                return True

    # Check negatively sloped diaganols
    for c in range(columns - 3):
        for r in range(3, rows):
            if board[r][c] == pos and board[r - 1][c + 1] == pos and board[r - 2][c + 2] == pos and board[r - 3][c + 3] == pos:
                return True


def main():
    board = construct_board(rows, columns)
    character = 'X'
    while True:
        display_board(board)
        print()
        print()
        if winning_move(board, character):
            print("player", character, "win")
            exit()
        pos = int(input("Please enter your position(1-7): "))
        if not insert_at(board, character, pos, rows):
            print("This is column is full try another column")
        if character == 'X':
            character = 'O'
        else:
            character = 'X'


main()

