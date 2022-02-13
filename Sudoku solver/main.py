def find_empty(bo):
    for row in range(9):
        for col in range(9):
            if bo[row][col] == 0:
                return row, col
    return -1, -1


def is_valid(bo, row, col, num):
    return check_row(bo, row, num) and check_col(bo, col, num) and check_box(bo, row, col, num)


def check_row(bo, row, num):
    if num in bo[row]:
        return False
    return True


def check_col(bo, col, num):
    for i in range(9):
        if bo[i][col] == num:
            return False
    return True


def check_box(bo, row, col, num):
    box_row, box_col = row - row % 3, col - col % 3
    for i in range(3):
        for j in range(3):
            if bo[box_row + i][box_col + j] == num:
                return False
    return True


def solve(bo):
    row, col = find_empty(bo)
    if row == -1 and col == -1:  # if there are no empty cells, we are done
        return True
    for num in range(1, 10):
        if is_valid(bo, row, col, num):  # check if this number can be put in that cell
            bo[row][col] = num
            if solve(bo):
                return True
            bo[row][col] = 0
    return False    # triggers backtracking


board = [[0, 0, 0, 0, 0, 0, 0, 0, 9],
         [0, 0, 2, 1, 0, 0, 0, 5, 7],
         [0, 3, 0, 0, 2, 0, 0, 0, 0],
         [0, 0, 0, 6, 0, 0, 3, 0, 0],
         [0, 0, 5, 0, 0, 0, 9, 0, 0],
         [0, 8, 0, 0, 0, 7, 0, 6, 5],
         [0, 0, 3, 7, 0, 0, 0, 1, 2],
         [4, 0, 0, 0, 0, 8, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 6, 0, 0]]

if solve(board):
    print("Solved")
    for x in range(9):
        print(board[x])
else:
    print("Cannot be solved :(")



