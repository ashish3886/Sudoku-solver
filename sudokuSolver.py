sudoku =    [[2, 5, 0, 0, 0, 3, 0, 9, 1], 
            [3, 0, 9, 0, 5, 0, 7, 2, 0], 
            [0, 0, 1, 0, 0, 6, 3, 0, 0], 
            [0, 0, 0, 0, 6, 8, 0, 0, 3], 
            [0, 1, 0, 0, 4, 0, 0, 0, 0], 
            [6, 0, 3, 0, 0, 0, 0, 5, 0], 
            [1, 3, 2, 0, 0, 0, 0, 7, 0], 
            [0, 0, 0, 0, 0, 4, 0, 6, 0], 
            [7, 6, 4, 0, 1, 0, 0, 0, 0]]


#In progress to make user defined input for sudoku 
# def sudoku_input:



def sudoku_board():
    
    for i in range(len(sudoku)):
        line = ""
        if i == 3 or i == 6:
            print("*********************")
        for j in range(len(sudoku[i])):
            if j == 3 or j == 6:
                line += "| "
            line += str(sudoku[i][j])+" "
        print(line)

def checkCells(sudoku, i, j, num):
    rowCheck = True
    columnCheck = True
    #Horizontal check if number is present or not
    for x in range(9):
        if num == sudoku[i][x]:
            rowCheck = False
            break
    if rowCheck:
        #Vertical check if number is present or not 
        for x in range(9):
            if num == sudoku[x][j]:
                columnCheck = False
                break
        if columnCheck:
            square_1 = 3*(i//3)
            square_2 = 3*(j//3)
            temp = []
            # To check if the number is present in sudoko square frame
            for x in range(square_1, square_1+3):
                for y in range(square_2, square_2+3):
                    temp.append(sudoku[x][y])
            if num in temp:
                return False
            else:
                return True
            
    return False

def findEmptyCells(sudoku):
    for x in range(9):
        for y in range(9):
            if sudoku[x][y] == 0:
                return x, y
    return -1, -1

def sudokuSolver(sudoku):
    i, j = findEmptyCells(sudoku)
    if i == -1:
        return True
    for num in range(1, 10):
        if checkCells(sudoku, i, j, num):
            sudoku[i][j] = num
            if sudokuSolver(sudoku):
                return True
            sudoku[i][j] = 0
    return False
                
sudokuSolver(sudoku)
sudoku_board()
