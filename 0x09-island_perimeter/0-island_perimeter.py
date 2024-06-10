#!/usr/bin/python3
"""
Module for solution of island perimeter problem.
"""


def island_perimeter(grid):
    """Solution"""
    if len(grid) == 0:
        return 0
    if len(grid[0]) == 0:
        return 0
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i != 0 and i != len(grid) - 1:
                    if j != 0 and j != len(grid[i]) - 1:
                        if grid[i - 1][j] == 1:
                            perimeter -= 1
                        if grid[i][j - 1] == 1:
                            perimeter -= 1
                        if grid[i][j + 1] == 1:
                            perimeter -= 1
                        if grid[i + 1][j] == 1:
                            perimeter -= 1
                    elif j == len(grid[i]) - 1:
                        if grid[i - 1][j] == 1:
                            perimeter -= 1
                        if grid[i][j - 1] == 1:
                            perimeter -= 1
                        if grid[i + 1][j] == 1:
                            perimeter -= 1
                    else:
                        if grid[i - 1][j] == 1:
                            perimeter -= 1
                        if grid[i][j + 1] == 1:
                            perimeter -= 1
                        if grid[i + 1][j] == 1:
                            perimeter -= 1
                elif i == len(grid) - 1:
                    if j != 0 and j != len(grid[i]) - 1:
                        if grid[i - 1][j] == 1:
                            perimeter -= 1
                        if grid[i][j - 1] == 1:
                            perimeter -= 1
                        if grid[i][j + 1] == 1:
                            perimeter -= 1
                    elif j == len(grid[i]) - 1:
                        if grid[i - 1][j] == 1:
                            perimeter -= 1
                        if grid[i][j - 1] == 1:
                            perimeter -= 1
                    else:
                        if grid[i][j + 1] == 1:
                            perimeter -= 1
                        if grid[i - 1][j] == 1:
                            perimeter -= 1
                else:
                    if j != 0 and j != len(grid[i]) - 1:
                        if grid[i + 1][j] == 1:
                            perimeter -= 1
                        if grid[i][j - 1] == 1:
                            perimeter -= 1
                        if grid[i][j + 1] == 1:
                            perimeter -= 1
                    elif j == len(grid[i]) - 1:
                        if grid[i][j - 1] == 1:
                            perimeter -= 1
                        if grid[i + 1][j] == 1:
                            perimeter -= 1
                    else:
                        if grid[i][j + 1] == 1:
                            perimeter -= 1
                        if grid[i + 1][j] == 1:
                            perimeter -= 1
    return perimeter
