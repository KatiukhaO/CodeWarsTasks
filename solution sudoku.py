"""
Sudoku Background
Sudoku is a game played on a 9x9 grid. The goal of the game is to fill all cells of the grid with digits from 1 to 9,
so that each column, each row, and each of the nine 3x3 sub-grids (also known as blocks) contain all of the digits from 1 to 9.
(More info at: http://en.wikipedia.org/wiki/Sudoku)

Sudoku Solution Validator
Write a function validSolution/ValidateSolution/valid_solution() that accepts a 2D array representing a Sudoku board,
and returns true if it is a valid solution, or false otherwise. The cells of the sudoku board may also contain 0's, which will represent empty cells. Boards containing one or more zeroes are considered to be invalid solutions.

The board is always 9 cells by 9 cells, and every cell only contains integers from 0 to 9.
"""


def valid_solution(board):
    rotate_board = [[i[j] for i in board] for j in range(9 - 1, -1, -1)]

    sector_line = []
    for _ in range(9):
        n=0
        inner = []
        for line in board[2*n+n : 3*n+3]:
            p=0
            for cell in line[2*p+p : 3*p+3]:
                inner.append(cell)
                p+=1
            n+=1
        sector_line.append(inner)

    if check_line_with_etalon(board) and check_line_with_etalon(rotate_board) and check_line_with_etalon(sector_line):
        return True
    else:
        return False


def check_line_with_etalon(board):
    flag = True
    etalon_line = [i for i in range(1, 10)]
    for line in board:
        if sorted(line) != etalon_line or 0 in line:
            flag = False
    return  flag




print(valid_solution([ [5, 3, 4, 6, 7, 8, 9, 1, 2],        #True
                        [6, 7, 2, 1, 9, 5, 3, 4, 8],
                        [1, 9, 8, 3, 4, 2, 5, 6, 7],
                        [8, 5, 9, 7, 6, 1, 4, 2, 3],
                        [4, 2, 6, 8, 5, 3, 7, 9, 1],
                        [7, 1, 3, 9, 2, 4, 8, 5, 6],
                        [9, 6, 1, 5, 3, 7, 2, 8, 4],
                        [2, 8, 7, 4, 1, 9, 6, 3, 5],
                        [3, 4, 5, 2, 8, 6, 1, 7, 9]]))


print(valid_solution([[5, 3, 4, 6, 7, 8, 9, 1, 2],              #False
                                   [6, 7, 2, 1, 9, 0, 3, 4, 9],
                                   [1, 0, 0, 3, 4, 2, 5, 6, 0],
                                   [8, 5, 9, 7, 6, 1, 0, 2, 0],
                                   [4, 2, 6, 8, 5, 3, 7, 9, 1],
                                   [7, 1, 3, 9, 2, 4, 8, 5, 6],
                                   [9, 0, 1, 5, 3, 7, 2, 1, 4],
                                   [2, 8, 7, 4, 1, 9, 6, 3, 5],
                                   [3, 0, 0, 4, 8, 1, 1, 7, 9]]))

print(valid_solution([[1, 3, 2, 5, 7, 9, 4, 6, 8]
                    ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                    ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                    ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                    ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                    ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                    ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                    ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                    ,[8, 7, 9, 6, 4, 2, 1, 3, 5]]))
