import random
import tkinter as tk


def init_board():
    board = list(range(1, 16)) + [None]
    random.shuffle(board)
    while not is_solvable(board):
        random.shuffle(board)
    return board


def is_solvable(board):
    inv_count = 0
    for i in range(len(board)):
        for j in range(i + 1, len(board)):
            if board[i] and board[j] and board[i] > board[j]:
                inv_count += 1
    return inv_count % 2 == 0


def draw_board(canvas, board):
    canvas.delete("all")
    for i, num in enumerate(board):
        if num:
            x = (i % 4) * 100
            y = (i // 4) * 100
            canvas.create_rectangle(x, y, x + 100, y + 100, fill="lightblue")
            canvas.create_text(x + 50, y + 50, text=str(num), font=("Arial", 40))


def move_tile(event, canvas, board):
    x, y = event.x // 100, event.y // 100
    index = x + y * 4
    if board[index]:
        for neighbor in [index - 1, index + 1, index - 4, index + 4]:
            if 0 <= neighbor < 16 and board[neighbor] is None:
                board[neighbor], board[index] = board[index], None
                draw_board(canvas, board)
                break


def main():
    root = tk.Tk()
    root.title("15 Puzzle Game")
    canvas = tk.Canvas(root, width=400, height=400)
    canvas.pack()
    board = init_board()
    draw_board(canvas, board)
    canvas.bind("<Button-1>", lambda event: move_tile(event, canvas, board))
    root.mainloop()


if __name__ == "__main__":
    main()
