import practice_boards
from typing import List, Tuple, Optional, Union
from random import randint

#---------------------------------------------------------
# BOARD VIEWER
#---------------------------------------------------------
def view_board(board: List[List[int]]) -> str:
    board_str = ""
    for i in range(len(board)):
        for j in range(len(board)):
            if (j + 1) % 3 == 0 and j != 0 and j + 1 != len(board):
                board_str += f" {board[i][j]} |"
            else:
                board_str += f" {board[i][j]} "
        board_str += '\n'
        if (i + 1) % 3 == 0 and i != 0 and i + 1 != len(board):
            board_str += f"{'-' * (len(board[i]) + (len(board) // 3) + 16)}\n"
    return board_str

#---------------------------------------------------------
# EMPTY SPOT LOCATER
#---------------------------------------------------------
def locate_empty(board: List[List[int]]) -> Optional[Tuple[int, int]]:
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                return (i, j)

#---------------------------------------------------------
# VALID NUMBER SELECTION CHECKER
#---------------------------------------------------------
def in_row(board: List[List[int]], row_num: int, number: int) -> bool:
    """
    PRECONDITIONS: 0 <= row_num < len(board) and 1 <= number <= 9
    Returns False if number is not in board[row_num], True if it is.
    >>> check_row([], 1)
    False
    >>> check_row([1], 1)
    True
    >>> check_row([4, 1, 2, 3, 6, 7, 8, 5], 9)
    False
    """
    return number in board[row_num]

def in_column(board: List[List[int]], col_num: int, number: int) -> bool:
    """
    PRECONDITIONS: 0 <= col_num < len(board) and 1 <= number <= 9
    Returns True if number is the column, False if the number is not in the column.
    """
    for row in board:
        if row[col_num] == number:
            return True
    return False

def in_square(board: List[List[int]], position: int, number: int) -> bool:
    """
    PRECONDITIONS: 0 <= position[0], position[1] < len(board) and 1 <= number <= 9
    """
    row_begin, col_begin = (position[0] // 3) * 3, (position[1] // 3) * 3
    row_end, col_end = row_begin + 3, col_begin + 3

    for i in range(row_begin, row_end):
        for j in range(col_begin, col_end):
            if board[i][j] == number:
                return True
    return False

def validity(board: List[List[int]], number: int, position: Tuple[int, int]) -> bool:
    row_num, col_num = position[0], position[1]

    # Checking if the number is in the row
    num_is_in_row = in_row(board, row_num, number)
    if num_is_in_row:
        return False
    
    # Checking if the number is in the column
    num_is_in_col = in_column(board, col_num, number)
    if num_is_in_col:
        return False
    
    # Checking if the number is in the square
    num_is_in_square = in_square(board, position, number)
    return not num_is_in_square # Since this is the last check, a conditional isn't required

#---------------------------------------------------------
# BACKTRACKING ALGORITHM
#---------------------------------------------------------
def solve_board(board: List[List[int]], random=False) -> None:
    position = locate_empty(board)
    if position is None:    # Base case is that the board is already solved.
        return True
    else:
        row_num, col_num = position[0], position[1]
        for i in range(1, 10): # Loops through the possible values 1-9 inclusive.
            if random:
                possible_number = randint(1, 9)
            else:
                possible_number = i
            if validity(board, possible_number, position):
                board[row_num][col_num] = possible_number

                if solve_board(board):
                    return True
                board[row_num][col_num] = 0
    board_str = view_board(board)
    write_to(board_str)
    return False

#---------------------------------------------------------
# Solutions Notetaking
#---------------------------------------------------------
def write_to(board_str: str) -> None:
    with open("solution.txt", "a") as solution:
        solution.write("<><><><><><><><><><><><><><><><><><><><><><><><><><><><><><>\n")
        solution.write(board_str)

#---------------------------------------------------------
# SOLVED CHECKER
#---------------------------------------------------------
def is_solved(board: List[List[int]]) -> Union[bool, str]:
    """
    Returns True if board is solved and False otherwise.
    """
    for i in range(len(board)):
        for j in range(len(board)):
            entry = board[i][j]
            board[i][j] = 0
            if not validity(board, entry, (i, j)):
                return f"Incorrect Solution.\n'{entry}' is not valid at ({i + 1}, {j + 1})"
            board[i][j] = entry
    return True
