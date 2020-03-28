# Maze Solver

## Description of the project.
A maze is a 2D matrix in which some cells are blocked. One of the cells is the source cell, from where we have to start. And another one of them is the destination, where we have to reach. We have to find a path from the source to the destination without moving into any of the blocked cells. To solve this puzzle, we first start with the source cell and move in a direction where the path is not blocked. If taken path makes us reach to the destination then the puzzle is solved else, we come back and change our direction of the path taken. We are going to implement the same logic in our code also

### Algorithm
Firstly, we will make a matrix to represent the maze, and the elements of the matrix will be either 0 or 1. 0 will represent the blocked cell and 1 will represent the cells in which we can move. The matrix for the maze shown above is:

1 1 0 1 1

1 1 1 1 0

0 0 0 1 0

0 0 1 1 1

1 0 0 0 1

Now, we will make one more matrix of the same dimension to store the solution. Its elements will also be either 0 or 1. 1 will represent the cells in our path and rest of the cells will be 0. The matrix representing the solution is:

1 0 0 0 0

1 1 1 1 0

0 0 0 1 0

0 0 0 1 1

0 0 0 0 1

Thus, we now have our matrices. Next, we will find a path from the source cell to the destination cell and the steps we will take are:

Check for the current cell, if it is the destination cell, then the puzzle is solved. If not, then we will try to move downward and see if we can move in the downward cell or not (to move in a cell it must be vacant and not already present in the path). If we can move there, then we will continue with the path taken to the next downward cell. If not, we will try to move to the rightward cell. And if it is blocked or taken, we will move upward. Similarly, if we can't move up as well, we will simply move to the left cell. If none of the four moves (down, right, up, or left) are possible, we will simply move back and change our current path (backtracking).

#### Execution
To run this Project in your device first install it from main.exe file the edit your desired input in the input.txt file and the run (run.bat) file and you will get you output in output.txt file with time and date history.

##### Modules Used
1 . argparse - For creating a Command line interface
2 . datetime - For date and time history.
