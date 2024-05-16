#!/usr/bin/python3
""" This is the 100-nqueen module
"""
import sys


def check_int(string):
    result = 1
    if string[0] == '0' and len(string) != 1:
        return 0
    for i in range(len(string)):
        if string[i] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            result = 0
            break
    return result


def bound_fun(mat):
    for i in range(len(mat)):
        sum_row = 0
        for j in range(len(mat)):
            sum_row += mat[i][j]
        if sum_row > 1:
            return 0

    for i in range(len(mat)):
        sum_col = 0
        for j in range(len(mat)):
            sum_col += mat[j][i]
        if sum_col > 1:
            return 0
    for i in range(len(mat)):
        for j in range(len(mat)):
            sum_diag2 = 0
            sum_diag1 = 0
            for k in range(len(mat) - j - i):
                sum_diag1 += mat[i + k][j + k]
                sum_diag2 += mat[len(mat) - 1 - i - k][j + k]
            if sum_diag1 > 1 or sum_diag2 > 1:
                return 0
    return 1


if len(sys.argv) == 1 or len(sys.argv) > 2:
    print("Usage: nqueens N")
    sys.exit(1)
if not check_int(sys.argv[1]):
    print("N must be a number")
    sys.exit(1)
if int(sys.argv[1]) < 4:
    print("N must be at least 4")
    sys.exit(1)
n = int(sys.argv[1])


def nqueens(n, start):
    s_matr = []
    for i in range(n):
        row1 = []
        for j in range(2):
            row1.append(0)
        s_matr.append(row1)

    q_track = {}
    for i in range(n):
        q_track[str(i + 1)] = 0

    place = 0
    board = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        board.append(row)

    i = 0
    j = start
    while place < n:
        while j == n:
            if q_track[str(i + 1)] == 0:
                place -= 1
                if i != 0:
                    i -= 1
                board[i][q_track[str(i + 1)]] = 0
                j = q_track[str(i + 1)] + 1
                q_track[str(i + 1)] = 0
            else:
                q_track[str(i + 1)] = 0
                place -= 1
                i -= 1
                board[i][q_track[str(i + 1)]] = 0
                j = q_track[str(i + 1)] + 1
        while j < n:
            board[i][j] = 1
            if bound_fun(board) == 0:
                board[i][j] = 0
                j += 1
            else:
                place += 1
                q_track[str(i + 1)] = j
                i += 1
                j = 0
                break
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                s_matr[i][0] = i
                s_matr[i][1] = j
    print(s_matr)


i = 0
if int(sys.argv[1]) == 4 or int(sys.argv[1]) == 6:
    i = 1
while i < int(sys.argv[1]) - 1:
    nqueens(n, i)
    i += 1
