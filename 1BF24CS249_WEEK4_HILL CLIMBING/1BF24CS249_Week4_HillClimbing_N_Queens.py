

N = 4

state = [3, 1, 2, 0]

def calculate_cost(state):
    cost = 0

    for i in range(N):
        for j in range(i + 1, N):

            if (state[i] == state[j] or
                abs(state[i] - state[j]) == abs(i - j)):

                cost += 1

    return cost

def generate_neighbors(state):
    neighbors = []

    for i in range(N):
        for j in range(i + 1, N):

            new_state = state.copy()

            new_state[i], new_state[j] = (
                new_state[j], new_state[i]
            )

            neighbors.append(new_state)

    return neighbors

def hill_climbing(state):

    current_state = state.copy()
    step = 1

    while True:

        current_cost = calculate_cost(current_state)

        print("\nIteration:", step)
        print("Current State:", current_state)
        print("Current Cost:", current_cost)

        if current_cost == 0:
            print("\nGoal State Reached!")
            return current_state

        neighbors = generate_neighbors(current_state)

        best_neighbor = None
        best_cost = float('inf')

        print("\nNeighbors and their costs:")

        for neighbor in neighbors:

            cost = calculate_cost(neighbor)

            print(neighbor, "Cost:", cost)

            if cost < best_cost:
                best_cost = cost
                best_neighbor = neighbor

        if best_cost >= current_cost:

            print("\nNo better neighbor found.")
            print("Algorithm terminated.")

            return current_state

        print("\nSelected Neighbor:", best_neighbor)
        print("Selected Cost:", best_cost)

        current_state = best_neighbor
        step += 1


print("Initial State:", state)

solution = hill_climbing(state)

print("\nFinal Solution:", solution)
print("Final Cost:", calculate_cost(solution))


# Output

# Initial State: [3, 1, 2, 0]

# Iteration: 1
# Current State: [3, 1, 2, 0]
# Current Cost: 2

# Neighbors and their costs:
# [1, 3, 2, 0] Cost: 1
# [2, 1, 3, 0] Cost: 1
# [0, 1, 2, 3] Cost: 6
# [3, 2, 1, 0] Cost: 6
# [3, 0, 2, 1] Cost: 1
# [3, 1, 0, 2] Cost: 1

# Selected Neighbor: [1, 3, 2, 0]
# Selected Cost: 1

# Iteration: 2
# Current State: [1, 3, 2, 0]
# Current Cost: 1

# Neighbors and their costs:
# [3, 1, 2, 0] Cost: 2
# [2, 3, 1, 0] Cost: 2
# [0, 3, 2, 1] Cost: 4
# [1, 2, 3, 0] Cost: 4
# [1, 0, 2, 3] Cost: 2
# [1, 3, 0, 2] Cost: 0

# Selected Neighbor: [1, 3, 0, 2]
# Selected Cost: 0

# Iteration: 3
# Current State: [1, 3, 0, 2]
# Current Cost: 0

# Goal State Reached!

# Final Solution: [1, 3, 0, 2]
# Final Cost: 0
