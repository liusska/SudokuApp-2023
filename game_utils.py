import copy


def is_valid_set(nums):
    num_set = set(nums)
    return len(num_set) == 9 and all(num in num_set for num in range(1, 10))


def convert_all_cells_values_in_int(original_grid):
    grid = copy.deepcopy(original_grid)
    for row in range(9):
        for col in range(9):
            if type(grid[row][col]) == str:
                grid[row][col] = int(grid[row][col])
    return grid


def is_any_empty_cell_in_grid(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == '':
                return True
    return False


def are_boxes_valid(grid):
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = [grid[box_row + i][box_col + j] for i in range(3) for j in range(3)]
            if not is_valid_set(box):
                return False
    return True


def are_rows_valid(grid):
    for row in grid:
        if not is_valid_set(row):
            return False
    return True


def is_sudoku_solved(grid):
    return (are_rows_valid(grid) and
            are_columns_valid(grid) and
            are_boxes_valid(grid))


def are_columns_valid(grid):
    for col in range(9):
        column = [grid[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False
    return True
