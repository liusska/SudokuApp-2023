import random


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


def view_sudoku_state(grid):
    """
    Print the current sudoku game state
    """
    for row in grid:
        print(' '.join([str(x) for x in row]))
    print('\n')


def solve_sudoku(numbers, index):
    if index == 81:
        return True

    row, col = divmod(index, 9)

    if sudoku_grid[row][col] != '':
        return solve_sudoku(numbers, index + 1)

    random.shuffle(numbers)
    for num in numbers:
        if is_valid_number(row, col, num):
            sudoku_grid[row][col] = num
            if solve_sudoku(numbers, index + 1):
                return True
            sudoku_grid[row][col] = ''
    return False


def is_valid_number(row, col, num):
    return (
        is_valid_row(row, num) and
        is_valid_column(col, num) and
        is_valid_box(row - row % 3, col - col % 3, num)
    )


def is_valid_row(row, num):
    return num not in sudoku_grid[row]


def is_valid_column(col, num):
    column = [sudoku_grid[row][col] for row in range(9)]
    return num not in column


def is_valid_box(start_row, start_col, num):
    box = [sudoku_grid[start_row + i][start_col + j] for i in range(3) for j in range(3)]
    return num not in box


def generate_solved_sudoku():
    numbers = list(range(1, 10))
    random.shuffle(numbers)
    solve_sudoku(numbers, 0)
    view_sudoku_state(sudoku_grid)


def remove_numbers(difficulty_level):
    # Calculate the number of cells to remove based on the difficulty level
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


def generate_start_numbers_for_sudoku():
    generate_solved_sudoku()
    # solved_sudoku = generate_solved_sudoku()

    difficulty_level = 'easy'  # Change this to 'medium' or 'hard' for different difficulty levels
    puzzle_grid = remove_numbers(difficulty_level)

    return puzzle_grid
    # return {
    #     'solved_sudoku': solved_sudoku,
    #     'puzzle_grid': puzzle_grid
    # }

# generate_start_numbers_for_sudoku()