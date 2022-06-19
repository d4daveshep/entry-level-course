# import pytest


def check_unique_9(group):
    for i in range(9):
        digit = str(i + 1)
        if digit not in group:
            return False
    return True


def is_valid_sudoku(grid):
    # first convert rows to strings and check for zeros
    rows = []
    for row in grid:
        row_string = str(row)
        if "0" in row_string: return False
        rows.append(row_string)

    # check if rows are OK first
    for row in rows:
        if not check_unique_9(row):
            return False

    # build the columns and check them
    cols = ["" for i in range(9)]
    for i in range(9):
        for j in range(9):
            cols[i] += (rows[j])[i]
            pass

    for col in cols:
        if not check_unique_9(col):
            return False

    # build 3x3 cells and check them
    cells = ["" for i in range(9)]
    for i in range(9):
        for j in range(9):
            cell_num = (j // 3) + 3 * (
                        i // 3)     # this took me ages to get this right - stop using trial and error and figure it out
                                    # mathematically
            digit = (rows[i])[j]
            cells[cell_num] += digit
            pass

    for cell in cells:
        if not check_unique_9(cell):
            return False

    return True


def test_check_unique_9():
    assert check_unique_9("876192543")
    assert not check_unique_9("123456788")


def test_is_valid_sudoku():
    valid_grid = [295743861,
                  431865927,
                  876192543,
                  387459216,
                  612387495,
                  549216738,
                  763524189,
                  928671354,
                  154938672]

    invalid_grid = [195743862,
                    431865927,
                    876192543,
                    387459216,
                    612387495,
                    549216738,
                    763524189,
                    928671354,
                    254938671]

    assert is_valid_sudoku(invalid_grid) == False
    assert is_valid_sudoku(valid_grid) == True
