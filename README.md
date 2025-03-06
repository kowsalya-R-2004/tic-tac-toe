
# Tic-Tac-Toe Game 🎮

This is a simple **Tic-Tac-Toe** game implemented in Python 🐍. It allows two players to play against each other in a console-based interface. The game alternates between two players (Player X and Player O) and checks for winning conditions after each move. 🎯

## Features ✨
- **Two-player gameplay**: Player X and Player O take turns to place their marks on the board 🤝.
- **Win condition check**: The game checks for winning conditions after each move (horizontal, vertical, and diagonal) 🏆.
- **Tie detection**: The game detects if the board is full and results in a tie 🏁.
- **Simple command-line interface**: The game is played entirely in the terminal/console ⌨️.

## How to Play 🕹️
1. Clone or download the repository 💾.
2. Open the terminal or command prompt 🖥️.
3. Navigate to the directory where the file is located 📂.
4. Run the script using the following command:

   ```bash
   python tic_tac_toe.py
   ```

5. The game will display a 3x3 grid 📊, and players will take turns entering their moves.
6. To make a move, enter the row and column number (from 0 to 2) where you'd like to place your mark ✏️.
7. The game will announce the winner or a tie at the end 🎉.

## Example of Gameplay 🤖

```
-------------
|   |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------

Player X's turn ❌
Enter row (0, 1, 2): 0
Enter column (0, 1, 2): 0
-------------
| X |   |   |
-------------
|   |   |   |
-------------
|   |   |   |
-------------

Player O's turn ⭕
Enter row (0, 1, 2): 1
Enter column (0, 1, 2): 1
-------------
| X |   |   |
-------------
|   | O |   |
-------------
|   |   |   |
-------------
...
```
