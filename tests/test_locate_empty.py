# Do this to be able to import from sudoku_board.py without getting warnings/errors
import sys
from os import getcwd
sys.path[0] = getcwd()

import unittest
from practice_boards import board1, board2, board4, TEST_BOARD, ALMOST_SOLVED_BOARD, SOLVED_BOARD # pylint: disable=import-error
from solver import locate_empty # pylint: disable=import-error

class TestLocateEmpty(unittest.TestCase):
    def test_locate_empty_one(self):
        answer = (0, 0)
        func_answer = locate_empty(board1)
        self.assertEqual(answer, func_answer)
    
    def test_locate_empty_two(self):
        answer = (0, 2)
        func_answer = locate_empty(board2)
        self.assertEqual(answer, func_answer)
    
    def test_locate_empty_four(self):
        answer = (0, 1)
        func_answer = locate_empty(board4)
        self.assertEqual(answer, func_answer)
    
    def test_locate_empty_TEST_BOARD(self):
        answer = (1, 0)
        func_answer = locate_empty(TEST_BOARD)
        self.assertEqual(answer, func_answer)
    
    def test_locate_empty_ALMOST_SOLVED_BOARD(self):
        answer = (8, 2)
        func_answer = locate_empty(ALMOST_SOLVED_BOARD)
        self.assertEqual(answer, func_answer)

    def test_locate_empty_SOLVED_BOARD(self):
        answer = None
        func_answer = locate_empty(SOLVED_BOARD)
        self.assertEqual(answer, func_answer)
    
if __name__ == "__main__":
    unittest.main()
