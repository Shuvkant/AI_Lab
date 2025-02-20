import queue
import copy

# Define the goal state
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Define possible moves (up, down, left, right)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def heuristic_misplaced(state):
    """Heuristic function: Number of misplaced tiles"""
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    # print(f"mis={misplaced}")
    return misplaced


def heuristic_manhattan(state):
    """Heuristic function: Manhattan distance"""
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(goal_x - i) + abs(goal_y - j)
    return distance


def is_solvable(state):
    """Check if the puzzle is solvable"""
    flattened = [tile for row in state for tile in row if tile != 0]
    inversions = sum(
        1
        for i in range(len(flattened))
        for j in range(i + 1, len(flattened))
        if flattened[i] > flattened[j]
    )
    return inversions % 2 == 0


def find_zero(state):
    """Find the position of the blank (zero) tile"""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def valid_moves(x, y):
    """Generate valid moves from the current blank tile position"""
    for dx, dy in MOVES:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            yield new_x, new_y


def a_star(start_state, heuristic):
    """A* search algorithm for solving the 8-puzzle problem"""
    if not is_solvable(start_state):
        return None, "Unsolvable puzzle"

    priority_queue = queue.PriorityQueue()
    # (f_score, state, g_score, path)
    priority_queue.put((0, start_state, 0, []))
    visited = set()

    while not priority_queue.empty():
        f_score, current_state, g_score, path = priority_queue.get()

        if current_state == GOAL_STATE:
            return path, "Solved"

        visited.add(tuple(tuple(row) for row in current_state))

        zero_x, zero_y = find_zero(current_state)

        for new_x, new_y in valid_moves(zero_x, zero_y):
            new_state = copy.deepcopy(current_state)
            new_state[zero_x][zero_y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[zero_x][zero_y]

            state_tuple = tuple(tuple(row) for row in new_state)
            if state_tuple in visited:
                continue

            new_path = path + [new_state]
            new_g_score = g_score + 1
            h_score = heuristic(new_state)
            priority_queue.put(
                (new_g_score + h_score, new_state, new_g_score, new_path))

    return None, "No solution found"


# Example usage
if __name__ == "__main__":
    start_state = [
        [1, 2, 6],
        [4, 0, 5],
        [7, 8, 3],
    ]

    heuristic = heuristic_manhattan  # You can switch to heuristic_misplaced
    solution, message = a_star(start_state, heuristic)

    if solution:
        print("Solution found!")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}:")
            for row in state:
                print(row)
            print()
    else:
        print(message)

print(f"Heuristic_misplaced={heuristic_misplaced(start_state)}")
print(f"Heuristic_manhatan={heuristic_manhattan(start_state)}")
