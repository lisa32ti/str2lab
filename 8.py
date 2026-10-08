def is_valid(matrix, row, col, num):
    for j in range(4):
        if matrix[row][j] == num:
            return False
    for i in range(4):
        if matrix[i][col] == num:
            return False
    box_row = (row // 2) * 2
    box_col = (col // 2) * 2
    for i in range(box_row, box_row + 2):
        for j in range(box_col, box_col + 2):
            if matrix[i][j] == num:
                return False
    return True


def find_empty(matrix):
    for i in range(4):
        for j in range(4):
            if matrix[i][j] == 0:
                return (i, j)
    return None


def solve_sudoku(matrix):
    empty = find_empty(matrix)
    if empty is None:
        return True

    row, col = empty
    for num in range(1, 5):
        if is_valid(matrix, row, col, num):
            matrix[row][col] = num
            if solve_sudoku(matrix):
                return True
            matrix[row][col] = 0
    return False


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(x) for x in row))


if __name__ == "__main__":
    puzzle = [
        [0, 0, 0, 0],
        [0, 0, 2, 0],
        [0, 1, 0, 0],
        [3, 0, 0, 4],
    ]

    print("Puzzle:")
    print_matrix(puzzle)
    print()

    if solve_sudoku(puzzle):
        print("Solution:")
        print_matrix(puzzle)
    else:
        print("No solution found.")