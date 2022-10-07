dashes = "---------"
pipe = "|"


def print_matrix(matrx):
    print(dashes)
    row = ""
    for i in range(len(matrx)):
        i += 1
        row += matrx[i - 1][0] + " "
        if i % 3 != 0:
            continue
        row = pipe + " " + row + pipe
        print(row)
        row = ""
    print(dashes)


def horizontal_check(matx):
    x_win, o_win = 0, 0
    if matx[0] == 'X' and matx[3] == 'X' and matx[6] == 'X':
        x_win = 1
    elif matx[1] == 'X' and matx[4] == 'X' and matx[7] == 'X':
        x_win = 1
    elif matx[2] == 'X' and matx[5] == 'X' and matx[8] == 'X':
        x_win = 1

    if matx[0] == 'O' and matx[3] == 'O' and matx[6] == 'O':
        o_win = 1
    elif matx[1] == 'O' and matx[4] == 'O' and matx[7] == 'O':
        o_win = 1
    elif matx[2] == 'O' and matx[5] == 'O' and matx[8] == 'O':
        o_win = 1

    if x_win == 1:
        return "X wins"
    elif o_win == 1:
        return "O wins"
    return None


def vert_diog_check(matx):
    x_win, o_win = 0, 0
    if matx[0] == 'X' and matx[1] == 'X' and matx[2] == 'X':
        x_win = 1
    elif matx[3] == 'X' and matx[4] == 'X' and matx[5] == 'X':
        x_win = 1
    elif matx[6] == 'X' and matx[7] == 'X' and matx[8] == 'X':
        x_win = 1
    elif matx[0] == 'X' and matx[4] == 'X' and matx[8] == 'X':
        x_win = 1
    elif matx[2] == 'X' and matx[4] == 'X' and matx[6] == 'X':
        x_win = 1

    if matx[0] == 'O' and matx[1] == 'O' and matx[2] == 'O':
        o_win = 1
    elif matx[3] == 'O' and matx[4] == 'O' and matx[5] == 'O':
        o_win = 1
    elif matx[6] == 'O' and matx[7] == 'O' and matx[8] == 'O':
        o_win = 1
    elif matx[0] == 'O' and matx[4] == 'O' and matx[8] == 'O':
        o_win = 1
    elif matx[2] == 'O' and matx[4] == 'O' and matx[6] == 'O':
        o_win = 1

    if x_win == 1:
        return "X wins"
    elif o_win == 1:
        return "O wins"
    else:
        return None


def general_check(matrx):
    whitespace = matrx.count([' '])
    general = horizontal_check(matrx)
    if general is None:
        general = vert_diog_check(matrx)
        if general is None and (whitespace == 0):
            return "Draw"
        else:
            return general
    else:
        return general


game_matrix = ['1 1', '1 2', '1 3',
               '2 1', '2 2', '2 3',
               '3 1', '3 2', '3 3']

matrix = [[" "], [" "], [" "], [" "], [" "], [" "], [" "], [" "], [" "]]  # initial matrix
print_matrix(matrix)

while True:
    white_space = matrix.count([' '])
    free_indexes = []
    for i in range(len(matrix)):
        if ' ' in matrix[i]:
            free_indexes.append(game_matrix[i])  # a list with free cells was created

    turn = input()
    check = turn.split()
    if (check[0].isdigit() is False) or (check[1].isdigit() is False):
        print("You should enter numbers!")
        continue
    elif int(check[0]) > 3 or int(check[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    elif turn not in free_indexes:
        print("This cell is occupied! Choose another one!")
        continue
    elif turn in free_indexes:
        index = game_matrix.index(turn)  # if the cell is free then the index of the list is determined
        if white_space % 2 != 0:
            matrix[index] = 'X'
        else:
            matrix[index] = 'O'
        print_matrix(matrix)
        result = general_check(matrix)
        if result is not None:
            print(result)
            break
