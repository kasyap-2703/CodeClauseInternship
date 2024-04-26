import random

def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

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

def available_moves(board):
    moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                moves.append((row, col))
    return moves

def ai_move(board):
    moves = available_moves(board)
    return random.choice(moves)

def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Unique Tic-Tac-Toe!")
    display_board(board)

    while True:
        player = players[turn % 2]

        if player == 'X':
            row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
            while not (0 <= row <= 2 and 0 <= col <= 2) or board[row][col] != ' ':
                print("Invalid move. Try again.")
                row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
        else:
            print("AI is making a move...")
            row, col = ai_move(board)

        board[row][col] = player
        display_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print("It's a tie!")
            break

        turn += 1

if __name__ == "__main__":
    main()
