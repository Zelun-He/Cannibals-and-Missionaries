from collections import deque

def is_valid(m_left, c_left):
    """Checks if the state is valid."""
    m_right, c_right = 3 - m_left, 3 - c_left
    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False  # Ensure values are within valid range
    return (m_left == 0 or m_left >= c_left) and (m_right == 0 or m_right >= c_right)

def get_successors(state):
    """Generates valid next states."""
    m, c, boat = state
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]  # Possible moves
    successors = []
    
    direction = -1 if boat == 1 else 1  # Moving left to right or vice versa

    for dm, dc in moves:
        new_m, new_c = m + direction * dm, c + direction * dc
        if is_valid(new_m, new_c):
            successors.append((new_m, new_c, 1 - boat))
    
    return successors

def solve():
    """Finds the optimal path using BFS."""
    initial_state = (3, 3, 1)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == (0, 0, 0):  # Goal reached
            return path + [state]
        if state not in visited:
            visited.add(state)
            for successor in get_successors(state):
                if successor not in visited:
                    queue.append((successor, path + [state]))
    
    return None  # No solution found

# Run the solver
path = solve()
if path:
    print("Optimal Path:")
    for step in path:
        print(step)
else:
    print("No solution found.")
