from games import *
from search import *
from utils import *
import math

# Connie Zhu, Evan Ng, Evan Yang
# Spring 2024 CPSC 481

# Change if you want :)
GRID_DIMENSION = 9

# For Improvement:
# COULD try backtracking to solve it

def heuristic_sudoku_empty_cells(node):
    """Heuristic function for Sudoku puzzles: Count the number of empty cells."""
    state = node.state
    empty_cells = sum(row.count(0) for row in state)  # Count empty cells in the Sudoku grid
    return empty_cells

class Sudoku(Problem):
    def __init__(self, initial=[[4,0,1,6,7,5,2,3,8],
                                [2,7,3,0,8,1,4,0,6],
                                [8,5,6,4,3,2,9,1,7],
                                [7,1,2,8,5,6,3,4,9],
                                [5,6,4,7,9,0,1,8,2],
                                [9,3,8,1,2,4,6,7,5],
                                [1,4,0,2,6,7,8,0,3],
                                [6,8,7,3,4,9,5,2,1],
                                [3,2,9,5,0,8,7,6,4]], goal = None):
        """ Define goal state and initialize a problem """
        super().__init__(initial, goal)

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
    
    def goal_test(self, state):
        def is_valid_state(state):
                return sorted(state) == list(range(1, GRID_DIMENSION+1))
            
        # Check rows
        for row in state:
            if not is_valid_state(row):
                return False
        
        # Check columns
        for col in range(GRID_DIMENSION):
            if not is_valid_state([state[row][col] for row in range(GRID_DIMENSION)]):
                return False
        
        # Check 3x3 subgrids
        for row in range(0, GRID_DIMENSION, int(math.sqrt(GRID_DIMENSION))):
            for col in range(0, GRID_DIMENSION, int(math.sqrt(GRID_DIMENSION))):
                subgrid = [state[r][c] for r in range(row, row + int(math.sqrt(GRID_DIMENSION))) for c in range(col, col + int(math.sqrt(GRID_DIMENSION)))]
                if not is_valid_state(subgrid):
                    return False
        
        return True

    def is_valid_move(self, state, i, j, num):
        """Check if placing the given number in the cell (i, j) is a valid move.
        Check if the number is not already in the same row, column, or 3x3 square"""
        return (
            not any(num == state[i][col] for col in range(GRID_DIMENSION)) and # checks rows
            not any(num == state[row][j] for row in range(GRID_DIMENSION)) and # checks column
            not any(num == state[row][col] for row in range(i//int(math.sqrt(GRID_DIMENSION))*int(math.sqrt(GRID_DIMENSION)), i//int(math.sqrt(GRID_DIMENSION))*int(math.sqrt(GRID_DIMENSION))+int(math.sqrt(GRID_DIMENSION))) # checks 2x2 square through integer division
                    for col in range(j//int(math.sqrt(GRID_DIMENSION))*int(math.sqrt(GRID_DIMENSION)), j//int(math.sqrt(GRID_DIMENSION))*int(math.sqrt(GRID_DIMENSION))+int(math.sqrt(GRID_DIMENSION))))
        )

if __name__ == '__main__':
    sudoku_instance = Sudoku()
    # Get the current state from the Sudoku instance
    current_state = sudoku_instance.initial

    # Get the possible actions for the current state AKA initial state
    possible_actions = sudoku_instance.actions(current_state)

    # Print the initial state
    for j in range(len(current_state[0])):
        row_values = [current_state[j][i] for i in range(len(current_state))]
        print("rows", j, ":", row_values)
    
    # possible actions
    print("Possible actions:", possible_actions)
    print("")

    # If experiencing None type error, ensure your initial state is correct
    # If you want to see the actions taken, set display to True
    print("DFS Solution:", depth_first_graph_search(sudoku_instance, display=True).solution()) 
    print("")
    print("BestFS Solution:", best_first_graph_search(sudoku_instance, heuristic_sudoku_empty_cells,display=True).solution())
    print("")
    print("AStar Solution:", astar_search(sudoku_instance, h=heuristic_sudoku_empty_cells, display=False).solution())
    print("")
    

    

    
