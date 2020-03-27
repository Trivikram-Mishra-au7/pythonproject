import argparse
import datetime

def MazePath(row, column):
    #if destination is reached, maze is solved
    #destination is the last cell(maze[SIZE-1][SIZE-1])
    if (row == SIZE - 1) and (column == SIZE - 1):
        solution[row][column] = 1
        return True
    #checking if we can visit in this cell or not
    #the indices of the cell must be in (0,SIZE-1)
    #and solution[r][c] == 0 is making sure that the cell is not already visited
    #maze[r][c] == 0 is making sure that the cell is not blocked
    if row>=0 and column>=0 and row<SIZE and column<SIZE and solution[row][column] == 0 and maze[row][column] == 1:
        #if safe to visit then visit the cell
        solution[row][column] = 1
        #going down
        if MazePath(row + 1, column):
            return True
        #going right
        if MazePath(row, column + 1):
            return True
        #going up
        if MazePath(row - 1, column):
            return True
        #going left
        if MazePath(row, column - 1):
            return True
        #backtracking
        solution[row][column] = 0
        return False
    return 0

def printSolution( sol ):
    f1.write("*\n" + "Following the path leads to the destination:\n\n")
    for i in sol:
        for j in i:
            f1.write(" " + str(j) + " ")
        f1.write('\n')
    now = datetime.datetime.now()
    f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S\n" + "*\n\n"))




if __name__ == "__main__":
    maze = []
    parser = argparse.ArgumentParser()
    parser.add_argument("ipFile", help = "Input file")
    parser.add_argument("opFile", help = "Output file")
    args = parser.parse_args()

    f = open(args.ipFile,'r')
    f1 = open(args.opFile,'a')

    for data in f:
        [l.strip('\n\r') for l in data]
        maze.append([int(x) for x in data.split()])

    SIZE = len(maze)
    solution = [[0] * SIZE for _ in range(SIZE)]

    if (MazePath(0, 0)):
        printSolution(solution)
    else:
        f1.write("***\n-1\n")
        f1.write("no solution for the maze.")
        now = datetime.datetime.now()
        f1.write("\nExecuted at: " + now.strftime("%Y-%m-%d*%H:%M:%S") + "\n***\n\n\n")

