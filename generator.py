from typing import List
from random import randint
from solver import solve_board, view_board, validity

def create_solved_board() -> List[List[int]]:
    new_board = [[0 for j in range(0, 9)] for k in range(0, 9)]
    solve_board(new_board, random=True)
    return new_board

def generate_board(difficulty: str) -> List[List[int]]:
    dif_to_rem = {
        "easy": (30, 49), 
        "medium": (50, 58), 
        "hard": (60, 64)
        }
    start_end_indices = dif_to_rem.get(difficulty.lower())
    if start_end_indices is not None:
        end = randint(start_end_indices[0], start_end_indices[1])
        solved_board = create_solved_board()
        removed_indices = []
        # Removes end number of values to generate the unsolved board
        for i in range(end): # pylint: disable=unused-variable
            remove_in = (randint(0, 8), randint(0, 8))
            while remove_in in removed_indices: # If the item is already 0, finds a new nonzero item to remove.
                remove_in = (randint(0, 8), randint(0, 8))
            removed_indices.append(remove_in)
            solved_board[remove_in[0]][remove_in[1]] = 0
    return solved_board
