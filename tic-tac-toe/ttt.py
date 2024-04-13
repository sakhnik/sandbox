#!/usr/bin/env python3

import random


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


def get_board_str(board):
    return "".join([cell for row in board for cell in row])


def prune(strategy, history):
    for i in range(-2, -len(history), -2):
        position, move = history[i]
        possible_moves = strategy.get(position)
        possible_moves.remove(move)
        if not possible_moves:
            break


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    history = []
    strategy = {}

    print("Welcome to Tic Tac Toe!")

    while True:
        print_board(board)
        key = input(f"Your move {current_player} (1-9): ")
        if key == '.':
            cur_board = get_board_str(board)
            possible_moves = strategy.get(cur_board)
            if not possible_moves:
                possible_moves = {(row, col)
                                  for row in range(3) for col in range(3)
                                  if board[row][col] == ' '}
                strategy[cur_board] = possible_moves
            row, col = random.choice(list(possible_moves))
        else:
            move = int(key)
            row = 2 - (move - 1) // 3
            col = (move - 1) % 3

        if board[row][col] != " ":
            print("Cell already occupied. Try again.")
            continue

        history.append((get_board_str(board), (row, col)))
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

    if check_win(board, current_player):
        prune(strategy, history)


if __name__ == "__main__":
    main()
