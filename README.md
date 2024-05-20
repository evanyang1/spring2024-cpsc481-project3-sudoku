# Spring 2024 CPSC 481 Project 3 Sudoku AI
Connie Zhu, Evan Ng, Evan Yang

This program solves a sudoku puzzle. You may choose the grid dimension whether it is 4 or 9. 

Using `search.py`, we create `sudoku.py` through the class Problem. After defining an actions, result, goal test, and valid action methods, we use algorithms such as depth first search to find a solution to the sudoku problem. 

Additionally, we created a heursitic function found in sudoku.py based on the number of empty cells in the puzzle.

# Execution
To run this code, please execute “py sudoku.py”, “python sudoku.py”, or “python3 sudoku.py” in a local terminal within the folder for this github repository.

# Purpose of Files
`sudoku.py` - python class Sudoku, extends Problem from `search.py`, main function for class Sudoku also included here
`search.py` - our algorithms are located in this file from aima-python, which is code from Russell And Norvig's Artificial Intelligence: A Modern Approach.
`utils.py` - utility file

