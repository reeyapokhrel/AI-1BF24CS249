from collections import deque
start = ((5, 4, 6),
         (1, 0, 8),
         (7, 3, 2))
goal = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))
def print_state(state):
    for row in state:
        print(row)
    print()
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def generate_moves(state):
    x, y = find_blank(state)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    children = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]
            children.append(tuple(tuple(row) for row in new_state))
    return children
def bfs(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    while queue:
        current, path = queue.popleft()
        if current == goal:
            return path
        for child in generate_moves(current):
            if child not in visited:
                visited.add(child)
                queue.append((child, path + [child]))
    return None
solution = bfs(start, goal)
if solution:
    print("INITIAL STATE\n")
    print_state(start)
    print("SOLUTION PATH\n")
    for i, state in enumerate(solution):
        print("Step", i)
        print_state(state)

    print("GOAL STATE REACHED")
    print("Total Steps =", len(solution) - 1)

else:
    print("No Solution Found")





