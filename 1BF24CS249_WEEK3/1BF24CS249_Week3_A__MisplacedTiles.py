import heapq

GOAL = (1,2,3,8," ",4,7,6,5)

def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()

def get_neighbors(state):
    neighbors = []

    blank_pos = state.index(" ")
    row = blank_pos // 3
    col = blank_pos % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_pos = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank_pos], new_state[new_pos] = \
                new_state[new_pos], new_state[blank_pos]

            neighbors.append(tuple(new_state))

    return neighbors

def manhattan_distance(state):
    distance = 0

    for index, tile in enumerate(state):
        if tile == " ":
            continue

        current_row = index // 3
        current_col = index % 3

        goal_index = GOAL.index(tile)

        goal_row = goal_index // 3
        goal_col = goal_index % 3

        distance += abs(current_row - goal_row)
        distance += abs(current_col - goal_col)

    return distance

def a_star(start):
    priority_queue = []
    counter = 0

    g = 0
    h = manhattan_distance(start)
    f = g + h

    heapq.heappush(
        priority_queue,
        (f, counter, g, start, [start])
    )

    cost_so_far = {start: 0}

    while priority_queue:

        f, _, g, current, path = heapq.heappop(priority_queue)

        if current == GOAL:
            return path

        for neighbor in get_neighbors(current):

            new_g = g + 1

            if neighbor not in cost_so_far or \
               new_g < cost_so_far[neighbor]:

                cost_so_far[neighbor] = new_g

                h = manhattan_distance(neighbor)
                new_f = new_g + h

                new_path = path + [neighbor]

                counter += 1

                heapq.heappush(
                    priority_queue,
                    (new_f, counter, new_g, neighbor, new_path)
                )

    return None

START = (2,8,3,1,6,4,7," ",5)


print("Initial State:")
print_puzzle(START)

print("Goal State:")
print_puzzle(GOAL)

path = a_star(START)

print("Solution:")
print()

for step, state in enumerate(path):

    g = step
    h = manhattan_distance(state)
    f = g + h

    print("Step:", step)
    print("g(n):", g)
    print("h(n):", h)
    print("f(n):", f)

    print_puzzle(state)

print("Total Moves:", len(path) - 1)

#Output

Initial State:
2 8 3
1 6 4
7   5

Goal State:
1 2 3
8   4
7 6 5

Solution:

Step: 0
g(n): 0
h(n): 5
f(n): 5
2 8 3
1 6 4
7   5

Step: 1
g(n): 1
h(n): 4
f(n): 5
2 8 3
1   4
7 6 5

Step: 2
g(n): 2
h(n): 3
f(n): 5
2   3
1 8 4
7 6 5

Step: 3
g(n): 3
h(n): 2
f(n): 5
  2 3
1 8 4
7 6 5

Step: 4
g(n): 4
h(n): 1
f(n): 5
1 2 3
  8 4
7 6 5

Step: 5
g(n): 5
h(n): 0
f(n): 5
1 2 3
8   4
7 6 5

Total Moves: 5
