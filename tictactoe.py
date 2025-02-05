import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False

def cell_clicked(row, col):
    global current_player, game_over

    if not game_over and board[row][col] == " ":
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        if check_winner(board, current_player):
            messagebox.showinfo("Winner", f"Player {current_player} wins!")
            game_over = True
        elif all(board[i][j] != " " for i in range(3) for j in range(3)):
            messagebox.showinfo("Tie", "It's a tie!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

def reset_game():
    global board, current_player, game_over
    for i in range(3):
        for j in range(3):
            board[i][j] = " "
            buttons[i][j].config(text=" ")
    current_player = "X"
    game_over = False

# Initialize board and other variables
board = [[" " for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False

# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create buttons for the board
buttons = [[None]*3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2,
                                  command=lambda row=i, col=j: cell_clicked(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)

# Create reset button
reset_button = tk.Button(root, text="Reset", font=("Arial", 12), width=10, command=reset_game)
reset_button.grid(row=3, column=1, pady=10)

# Start the GUI
root.mainloop()