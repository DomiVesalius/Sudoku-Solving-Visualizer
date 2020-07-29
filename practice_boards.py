board1 = [
    [0, 0, 4, 0, 1, 0, 5, 0, 0],
    [0, 1, 0, 0, 2, 0, 0, 3, 0],
    [5, 0, 0, 4, 0, 3, 0, 0, 2],
    [0, 0, 2, 0, 0, 0, 6, 0, 0],
    [7, 8, 0, 0, 9, 0, 0, 4, 5],
    [0, 0, 5, 0, 0, 0, 7, 0, 0],
    [9, 0, 0, 8, 0, 1, 0, 0, 6],
    [0, 7, 0, 0, 6, 0, 0, 5, 0],
    [0, 0, 8, 0, 4, 0, 9, 0, 0]
]

board2 = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 7, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

board3 = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

board4 = [
    [9, 0, 2, 0, 0, 0, 0, 5, 3],
    [0, 8, 0, 0, 0, 2, 0, 0, 0],
    [2, 6, 3, 1, 0, 0, 0, 0, 9],
    [0, 0, 0, 9, 0, 0, 0, 6, 0],
    [0, 5, 0, 3, 0, 6, 0, 0, 2],
    [0, 0, 0, 0, 0, 0, 4, 0, 5],
    [0, 2, 8, 0, 0, 3, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 7, 0, 0]
]

board5 = [
    [0, 0, 0, 0, 8, 4, 0, 2, 0],
    [8, 4, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 8],
    [1, 0, 0, 0, 3, 0, 0, 0, 0],
    [9, 0, 0, 4, 0, 0, 2, 0, 7],
    [0, 5, 0, 0, 0, 6, 0, 0, 0],
    [0, 7, 0, 0, 0, 0, 0, 8, 0],
    [6, 0, 0, 0, 5, 0, 1, 7, 0],
    [0, 0, 8, 0, 0, 7, 0, 9, 0]
]

board6 = [
    [9, 6, 0, 0, 4, 0, 1, 0, 0],
    [0, 0, 0, 3, 8, 0, 0, 0, 0],
    [7, 0, 8, 0, 6, 0, 0, 0, 9],
    [1, 2, 0, 8, 0, 0, 9, 0, 3],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [3, 0, 5, 0, 0, 2, 0, 6, 4],
    [8, 0, 0, 0, 9, 0, 4, 0, 7],
    [0, 0, 0, 0, 3, 8, 0, 0, 0],
    [0, 0, 9, 0, 2, 0, 0, 8, 5]
]

TEST_BOARD = [
    [9, 6, 2, 5, 4, 3, 1, 7, 8],
    [0, 0, 0, 3, 8, 0, 0, 0, 0],
    [7, 0, 8, 0, 6, 0, 0, 0, 9],
    [1, 2, 0, 8, 0, 0, 9, 0, 3],
    [0, 0, 0, 0, 5, 0, 0, 0, 0],
    [3, 0, 5, 0, 0, 2, 0, 6, 4],
    [8, 0, 0, 0, 9, 0, 4, 0, 7],
    [0, 0, 0, 0, 3, 8, 0, 0, 0],
    [0, 0, 9, 0, 2, 0, 0, 8, 5]
]

SOLVED_BOARD = [
    [1, 8, 4, 9, 6, 3, 7, 2, 5],
    [5, 6, 2, 7, 4, 8, 3, 1, 9],
    [3, 9, 7, 5, 1, 2, 8, 6, 4],
    [2, 3, 9, 6, 5, 7, 1, 4, 8],
    [7, 5, 6, 1, 8, 4, 2, 9, 3],
    [4, 1, 8, 2, 3, 9, 6, 5, 7],
    [9, 4, 1, 3, 7, 6, 5, 8, 2],
    [6, 2, 3, 8, 9, 5, 4, 7, 1],
    [8, 7, 5, 4, 2, 1, 9, 3, 6]
]

ALMOST_SOLVED_BOARD = [
    [1, 8, 4, 9, 6, 3, 7, 2, 5],
    [5, 6, 2, 7, 4, 8, 3, 1, 9],
    [3, 9, 7, 5, 1, 2, 8, 6, 4],
    [2, 3, 9, 6, 5, 7, 1, 4, 8],
    [7, 5, 6, 1, 8, 4, 2, 9, 3],
    [4, 1, 8, 2, 3, 9, 6, 5, 7],
    [9, 4, 1, 3, 7, 6, 5, 8, 2],
    [6, 2, 3, 8, 9, 5, 4, 7, 1],
    [8, 7, 0, 4, 2, 1, 9, 3, 6]
]