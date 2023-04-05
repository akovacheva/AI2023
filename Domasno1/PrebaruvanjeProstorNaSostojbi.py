
initial_state_yellow = [(3, 1), (4, 1)]
initial_state_green = [(1, 5), (2, 5)]


def goal_test(self, state):
    goal_state_yellow = sorted(initial_state_green)
    goal_state_green = sorted(initial_state_yellow)
    for position in goal_state_yellow:
        if position  not in goal_state_green:
            return False
    return True


def move_pacman(pacman_pos, direction, board):

    row, col = pacman_pos
    new_row, new_col = row, col
    if direction == 'up':
        new_row -= 1
    elif direction == 'down':
        new_row += 1
    elif direction == 'left':
        new_col -= 1
    elif direction == 'right':
        new_col += 1
    else:
        raise ValueError(f"Invalid direction '{direction}', must be one of 'up', 'down', 'left', or 'right'")

    # Check if new position is in bounds
    if new_row < 0 or new_row >= len(board) or new_col < 0 or new_col >= len(board[0]):
        return None, board

    # Check if new position is already occupied
    if board[new_row][new_col] is not None:
        return None, board

    # Check if Pacman would have to jump over another Pacman
    if direction == 'up':
        for r in range(row - 1, new_row - 1, -1):
            if board[r][col] is not None:
                return None, board
    elif direction == 'down':
        for r in range(row + 1, new_row + 1):
            if board[r][col] is not None:
                return None, board
    elif direction == 'left':
        for c in range(col - 1, new_col - 1, -1):
            if board[row][c] is not None:
                return None, board
    elif direction == 'right':
        for c in range(col + 1, new_col + 1):
            if board[row][c] is not None:
                return None, board

    # Move Pacman to new position
    new_board = [row[:] for row in board]
    new_board[row][col] = None
    new_board[new_row][new_col] = board[row][col]
    return (new_row, new_col), new_board
