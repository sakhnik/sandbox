#!/usr/bin/env python


def print_board(board):
    first = True
    for row in board:
        if not first:
            print("──┼───┼──")
        first = False
        print(" │ ".join(row))


def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        move = int(input("Your move (1-9): "))
        row = 2 - (move - 1) // 3
        col = (move - 1) % 3
        print(f"row={row} col={col}")

        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
