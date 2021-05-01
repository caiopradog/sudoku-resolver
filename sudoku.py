import time
import math

"""
Solved Sudoku
[8, 2, 7, 1, 5, 4, 3, 9, 6],
[9, 6, 5, 3, 2, 7, 1, 4, 8],
[3, 4, 1, 6, 8, 9, 7, 5, 2],
[5, 9, 3, 4, 6, 8, 2, 7, 1],
[4, 7, 2, 5, 1, 3, 6, 8, 9],
[6, 1, 8, 9, 7, 2, 4, 3, 5],
[7, 8, 6, 2, 3, 5, 9, 1, 4],
[1, 5, 4, 7, 9, 6, 8, 2, 3],
[2, 3, 9, 8, 4, 1, 5, 6, 7],

Clean Sudoku
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0],
"""

grid = [
    [4, 0, 6, 0, 0, 0, 0, 5, 1],
    [0, 1, 0, 0, 0, 0, 0, 0, 0],
    [7, 0, 0, 6, 0, 0, 0, 8, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 7, 0, 0, 0, 0, 0],
    [8, 2, 0, 0, 1, 0, 0, 5, 0],
    [0, 0, 0, 8, 7, 3, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 2, 0],
    [0, 0, 5, 9, 0, 0, 3, 0, 0],
]

solutionGrid = []
for xPosGrid in range(9):
    solutionGrid.append([])
    for yPosGrid in range(9):
        solutionGrid[xPosGrid].append([1, 2, 3, 4, 5, 6, 7, 8, 9])


def checkRows():
    global grid

    for xPos in range(9):
        row = grid[xPos]
        if len(list(set(row))) < 9:
            return False
    return True


def checkColumns():
    global grid

    for yPos in range(9):
        column = [
            grid[0][yPos],
            grid[1][yPos],
            grid[2][yPos],
            grid[3][yPos],
            grid[4][yPos],
            grid[5][yPos],
            grid[6][yPos],
            grid[7][yPos],
            grid[8][yPos],
        ]
        if len(list(set(column))) < 9:
            return False
    return True


def checkMiniGrid():
    global grid

    for xPos in range(3):
        for yPos in range(3):
            miniGrid = [
                grid[(xPos * 3)][(yPos * 3)],
                grid[(xPos * 3)][(yPos * 3) + 1],
                grid[(xPos * 3)][(yPos * 3) + 2],
                grid[(xPos * 3) + 1][(yPos * 3)],
                grid[(xPos * 3) + 1][(yPos * 3) + 1],
                grid[(xPos * 3) + 1][(yPos * 3) + 2],
                grid[(xPos * 3) + 2][(yPos * 3)],
                grid[(xPos * 3) + 2][(yPos * 3) + 1],
                grid[(xPos * 3) + 2][(yPos * 3) + 2],
            ]
            if len(list(set(miniGrid))) < 9:
                return False
    return True


def isSolved():
    return checkRows() and checkColumns() and checkMiniGrid()


def solveGrid():
    global grid

    for xPos in range(9):
        for yPos in range(9):
            num = grid[xPos][yPos]
            if num > 0:
                removePossibleNums(num, xPos, yPos)


def removePossibleNums(num, xPos, yPos):
    for x in range(9):
        removeNumFromSolveGrid(num, x, yPos)
        removeNumFromSolveGrid(num, xPos, x)

    miniGridX = math.floor(xPos / 3) * 3
    miniGridY = math.floor(yPos / 3) * 3
    for x in range(miniGridX, miniGridX + 3):
        for y in range(miniGridY, miniGridY + 3):
            removeNumFromSolveGrid(num, x, y)


def removeNumFromSolveGrid(num, xPos, yPos):
    global grid
    global solutionGrid

    if grid[xPos][yPos] != num and num in solutionGrid[xPos][yPos]:
        solutionGrid[xPos][yPos].remove(num)
        if len(solutionGrid[xPos][yPos]) == 1:
            grid[xPos][yPos] = solutionGrid[xPos][yPos][0]


def cleanSolutionGrid():
    global grid
    global solutionGrid

    for xPos in range(9):
        for yPos in range(9):
            num = grid[xPos][yPos]
            if num > 0:
                solutionGrid[xPos][yPos] = [num]


cleanSolutionGrid()
oldSolutionGridSum = []
while not isSolved():
    solveGrid()
    for x in range(9):
        print(grid[x])
    print('--------------------------------')
    for x in range(9):
        print(solutionGrid[x])
    print('--------------------------------')
    solutionGridSum = sum(sum(solutionGrid, []), [])
    if len(solutionGrid) == len(oldSolutionGridSum):
        print("I'm Stuck :(")
        break;
    oldSolutionGridSum = solutionGrid
    time.sleep(1)

if isSolved():
    for x in range(9):
        print(grid[x])
    print('Solved! :)')
