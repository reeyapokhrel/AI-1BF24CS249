
import random
import math

def calculate_cost(board):
    conflicts = 0
    n = len(board)

    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j]:
                conflicts += 1
            elif abs(board[i] - board[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def get_neighbor(board):
    new_board = board.copy()

    col = random.randint(0, 7)
    new_row = random.randint(0, 7)

    new_board[col] = new_row

    return new_board


def simulated_annealing():
    n = 8

    board = [random.randint(0, 7) for _ in range(n)]

    temperature = 100
    cooling_rate = 0.99
    min_temperature = 0.001

    current_cost = calculate_cost(board)

    while temperature > min_temperature:

        if current_cost == 0:
            break

        new_board = get_neighbor(board)
        new_cost = calculate_cost(new_board)

        delta = new_cost - current_cost

        if delta < 0:
            board = new_board
            current_cost = new_cost

        elif random.random() < math.exp(-delta / temperature):
            board = new_board
            current_cost = new_cost

        temperature *= cooling_rate

    return board, current_cost


def display_board(board):
    print("\nChessboard:")

    for row in range(8):
        for col in range(8):
            if board[col] == row:
                print(" Q ", end="")
            else:
                print(" . ", end="")
        print()


solution, cost = simulated_annealing()

print("Final Board:")
display_board(solution)

print("\nFinal Cost:", cost)

if cost == 0:
    print("Solution Found!")
else:
    print("Solution Not Found. Try Again.")


# Output
# Final Board:

# Chessboard:
#  .  .  .  .  .  Q  .  . 
#  .  .  .  Q  .  .  .  . 
#  .  .  .  .  .  .  Q  . 
#  Q  .  .  .  .  .  .  . 
#  .  .  .  .  .  .  .  Q 
#  .  Q  .  .  .  .  .  . 
#  .  .  .  .  Q  .  .  . 
#  .  .  Q  .  .  .  .  . 

# Final Cost: 0
# Solution Found!
