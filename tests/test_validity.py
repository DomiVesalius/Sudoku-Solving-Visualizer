# Do this to be able to import from sudoku_board.py without getting warnings/errors
import sys
from os import getcwd
sys.path[0] = getcwd()

import unittest
from practice_boards import board1, board2, board4, TEST_BOARD, ALMOST_SOLVED_BOARD, SOLVED_BOARD # pylint: disable=import-error
from solver import validity # pylint: disable=import-error

class TestValidity(unittest.TestCase):
    def test_validity_one(self):
        answer = True
        func_answer = validity(board1, 2, (0, 0))
        self.assertEqual(func_answer, answer)

    def test_validity_column(self):
        answer = False
        func_answer = validity(board1, 7, (0, 0))
        self.assertEqual(func_answer, answer)

    def test_validity_row(self):
        answer = False
        func_answer = validity(board1, 9, (2, 6))
        self.assertEqual(func_answer, answer)

    def test_validity_ALMOST_SOLVED_BOARD(self):
        answer = True
        func_answer = validity(ALMOST_SOLVED_BOARD, 5, (8, 2))
        self.assertEqual(func_answer, answer)

    def test_validity_ALMOST_SOLVED_BOARD2(self):
        answer = False
        func_answer = validity(ALMOST_SOLVED_BOARD, 6, (8, 2))
        self.assertEqual(func_answer, answer)

if __name__ == "__main__":
    unittest.main()