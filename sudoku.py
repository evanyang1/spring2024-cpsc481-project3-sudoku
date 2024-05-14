from games import *
from search import *
from utils import *

GRID_DIMENSION = 9

# TODO: try other algorithms to find the best one
# COULD backtracking to solve it
# create own dfs

# ----------------------------------------------------------------
# PROFESSOR FEEDBACK #
# remove goal parameter
# instead, create a function to check, each and every list does not have 0s, and matches sudoku rules
# goal state would be no 0s in the board 
    # still have to follow the rules of sudoku
    # check whether goal state is right or wrong
# skip giving goal state, because easier to generate action
# do it each cell by cell or block by block
# goal can be empty node set
# goal state would be no 0s in the board 
    # still have to follow the rules of sudoku
    # check whether goal state is right or wrong
# instead, create a function to check, each and every list does not have 0s, and matches sudoku rules

class Sudoku(Problem):
    def __init__(self, initial=[[0,0,0,1,0,0,2,0,4],
                                [0,0,7,5,8,6,9,1,3],
                                [0,1,0,3,0,0,0,0,7],
                                [0,3,0,6,5,0,4,7,9],
                                [0,0,8,7,0,3,0,6,2],
                                [0,0,0,2,0,0,5,0,8],
                                [8,7,0,0,0,0,0,0,0],
                                [0,4,9,0,1,0,0,2,0],
                                [2,5,0,4,0,0,8,9,0]]):
        """ Define goal state and initialize a problem """
        super().__init__(initial)

    def actions(self,state):
        """Return a list of possible actions (i.e., possible numbers to fill in)
        for empty cells in the Sudoku grid."""
        actions = []
        for i in range(GRID_DIMENSION):
            for j in range(GRID_DIMENSION):
                if state[i][j] == 0:  # If the cell is empty
                    for num in range(1, GRID_DIMENSION + 1): 
                        if self.is_valid_move(state, i, j, num):
                            actions.append((i, j, num))
        return actions
    
    def result(self, state, action):
        """Return the new state after applying the given action."""
        i, j, num = action
        new_state = [row[:] for row in state]  # Copy the current state
        new_state[i][j] = num  # Place the number in the cell
        return new_state
    
    def is_valid_move(self, state, i, j, num):
        """Check if placing the given number in the cell (i, j) is a valid move.
        Check if the number is not already in the same row, column, or 3x3 square"""
        return (
            not any(num == state[i][col] for col in range(GRID_DIMENSION)) and # checks rows
            not any(num == state[row][j] for row in range(GRID_DIMENSION)) and # checks column
            not any(num == state[row][col] for row in range(i//3*3, i//3*3+3) # checks 2x2 square through integer division
                    for col in range(j//3*3, j//3*3+3))
        )

if __name__ == '__main__':
    sudoku_instance = Sudoku()
    # Get the current state from the Sudoku instance
    current_state = sudoku_instance.initial

    # Get the possible actions for the current state
    possible_actions = sudoku_instance.actions(current_state)
    
    # Print the possible actions
    for j in range(len(current_state[0])):
        row_values = [current_state[j][i] for i in range(len(current_state))]
        print("rows", j, ":", row_values)
    print("Possible actions:", possible_actions)

    # assigns solution
    # solution = depth_first_graph_search(sudoku_instance).solution()

    # does both
    print(depth_first_graph_search(sudoku_instance).solution()) 
    
    # solution = depth_first_tree_search(sudoku_instance).solution()
    # print(solution)


    

    
