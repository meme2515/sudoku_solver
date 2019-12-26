# 🎲 Sudoku Solver

This is a simple project with an automated sudoku solver and a pygame based GUI interface.
Project concept is based on techwithtim's GUI-solver project: https://github.com/techwithtim/Sudoku-GUI-Solver

## 💻 Backtracking Algorithm

The main 'solve' algorithm is based on the backtracking algorithm, which aims to find a solution to a problem by eliminating one possibility at a time. Different possibilities are laid out in order through recursion. The bulk of the text-based solver implementation can be found in solver.py.

Details about the backtracking algorithm can be found in this link: https://www.geeksforgeeks.org/backtracking-algorithms/

## 🎮 Pygame

Pygame is a Python module designed for video game production. In this project, I have implemented the module to create a GUI version of the game of sudoku. In it, you have the option to either play and actual game of sudoku or turn to an automated solution generator.

![Alt text](Capture.jpg?raw=true)
