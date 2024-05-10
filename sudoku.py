from games import *
from search import *
from utils import *

# TODO: try other algorithms to find the best one
# TODO: bigger board?

# goal can be empty node set
# goal state would be no 0s in the board 
    # still have to follow the rules of sudoku
    # check whether goal state is right or wrong

# avoid defining the goal state

# COULD backtracking to solve it
# create own dfs
# remove goal parameter
# instead, create a function to check, each and every list does not have 0s, and matches sudoku rules

class Sudoku(Problem):
    def __init__(self, initial=[[1,2,0,4],[4,0,0,1],[2,0,1,3],[0,0,4,0]], goal=[[1,2,3,4],[4,3,2,1],[2,4,1,3],[3,1,4,2]]):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

    def actions(self,state):
        """Return a list of possible actions (i.e., possible numbers to fill in)
        for empty cells in the Sudoku grid."""
        actions = []
        for i in range(4):
            for j in range(4):
                if state[i][j] == 0:  # If the cell is empty
                    for num in range(1, 5):  # Try numbers 1 to 4
                        if self.is_valid_move(state, i, j, num):
                            actions.append((i, j, num))
        return actions
    
    def result(self, state, action):
        """Return the new state after applying the given action."""
        i, j, num = action
        new_state = [row[:] for row in state]  # Copy the current state
        new_state[i][j] = num  # Place the number in the cell
        return new_state

    def goal_test(self, state):
        # edit this
        return state == self.goal
    
    def is_valid_move(self, state, i, j, num):
        """Check if placing the given number in the cell (i, j) is a valid move.
        Check if the number is not already in the same row, column, or 2x2 square"""
        return (
            not any(num == state[i][col] for col in range(4)) and # checks rows
            not any(num == state[row][j] for row in range(4)) and # checks column
            not any(num == state[row][col] for row in range(i//2*2, i//2*2+2) # checks 2x2 square through integer division
                    for col in range(j//2*2, j//2*2+2))
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


    

    
