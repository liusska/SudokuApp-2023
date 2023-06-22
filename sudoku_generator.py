import random


def view_sudoku_state(grid):
    """
    Print the current sudoku game state
    """
    for row in grid:
        print(' '.join([str(x) for x in row]))
    print('\n')


def solve_sudoku(sudoku_grid, numbers, index):
    """
    Recursively solves a Sudoku grid using backtracking.
    Returns True if a solution is found, False otherwise.
    """
    if index == 81:
        return True

    row, col = divmod(index, 9)

    if sudoku_grid[row][col] != '':
        return solve_sudoku(sudoku_grid, numbers, index + 1)

    random.shuffle(numbers)
    for num in numbers:
        if is_valid_number(sudoku_grid, row, col, num):
            sudoku_grid[row][col] = num
            if solve_sudoku(sudoku_grid, numbers, index + 1):
                return True
            sudoku_grid[row][col] = ''
    return False


def is_valid_number(sudoku_grid, row, col, num):
    """Check if the number already exists in the selected row, column and box"""
    return (
        is_valid_row(sudoku_grid, row, num) and
        is_valid_column(sudoku_grid, col, num) and
        is_valid_box(sudoku_grid, row - row % 3, col - col % 3, num)
    )


def is_valid_row(sudoku_grid, row, num):
    """ Check if the number already exists in the row"""
    return num not in sudoku_grid[row]


def is_valid_column(sudoku_grid, col, num):
    """ Check if the number already exists in the column """
    column = [sudoku_grid[row][col] for row in range(9)]
    return num not in column


def is_valid_box(sudoku_grid, start_row, start_col, num):
    """ Check if the number already exists in valid 3x3 box """
    box = [sudoku_grid[start_row + i][start_col + j] for i in range(3) for j in range(3)]
    return num not in box


def generate_solved_sudoku(sudoku_grid):
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    solve_sudoku(sudoku_grid, numbers, 0)
    view_sudoku_state(sudoku_grid)


def remove_numbers(sudoku_grid, difficulty_level):
    """Calculate the number of cells to remove random based on the difficulty level"""

    if difficulty_level == 'easy':
        cells_to_remove = 40
    elif difficulty_level == 'medium':
        cells_to_remove = 50
    elif difficulty_level == 'hard':
        cells_to_remove = 60
    else:
        cells_to_remove = 0

    # Create a copy of the generated Sudoku grid
    puzzle = [row[:] for row in sudoku_grid]

    # Generate a list of cell indices
    indices = [(row, col) for row in range(9) for col in range(9)]

    # Randomly remove cells from the puzzle
    random.shuffle(indices)
    for i in range(cells_to_remove):
        row, col = indices[i]
        puzzle[row][col] = ''

    return puzzle


def generate_start_numbers_for_sudoku(difficulty_level):
    """
    Initialize new sudoku grid puzzle by difficulty level ('easy', 'medium' or 'hard').
    The new grid is based on generated solved sudoku with hidden cells.
    """

    sudoku_grid = [
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', ''],
        ['', '', '', '', '', '', '', '', '']
    ]
    generate_solved_sudoku(sudoku_grid)

    puzzle_grid = remove_numbers(sudoku_grid, difficulty_level)
    view_sudoku_state(puzzle_grid)
    return puzzle_grid
