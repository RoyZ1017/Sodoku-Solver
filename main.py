import time
start = time.time()

# initialize the board
board = [
    [4, 0, 0, 0, 5, 0, 0, 0, 0],
    [8, 7, 0, 0, 0, 3, 0, 0, 9],
    [0, 3, 0, 8, 6, 0, 0, 0, 7],
    [0, 0, 0, 0, 0, 0, 1, 0, 5],
    [0, 0, 0, 0, 9, 0, 0, 0, 0],
    [7, 1, 0, 0, 0, 4, 0, 0, 3],
    [0, 2, 0, 0, 0, 6, 9, 7, 0],
    [0, 0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 9, 2, 0, 4]
]

solved_pieces = []  # numbers given at the start of the game
board_idx = []  # index to start at after backtracking
for i in range(0, 9):
    row_idx = []
    for j in range(0, 9):
        row_idx.append(0)
        if board[i][j] != 0:
            solved_pieces.append([i, j])
    board_idx.append(row_idx)

# check if board is solved
def solved(board):
    for row in board:
        if 0 in row:
            return False
    return True

def valid_nums(row, col, board):
    valid = [i for i in range(1, 10)]

    # row
    for c in range(len(board[row])):
        if c != col:
            if board[row][c] in valid:
                valid.remove(board[row][c])

    # col
    for r in range(len(board)):
        if r != row:
            if board[r][col] in valid:
                valid.remove(board[r][col])

    # quadrant
    quadrant = [row//3, col//3]
    for i in range(quadrant[0] * 3, quadrant[0] * 3 + 3):
        for j in range(quadrant[1] * 3, quadrant[1] * 3 + 3):
            if i != row and j != col:
                if board[i][j] in valid:
                    valid.remove(board[i][j])

    return valid

def move_forward(coord):
    if coord[1] < 8:
        coord[1] += 1
    else:
        coord = [coord[0] + 1, 0]
    return coord

def move_back(coord):
    if coord[1] > 0:
        coord[1] -= 1
    else:
        coord = [coord[0] - 1, 8]
    return coord

curr_coord = [0, 0]
forward = True

while not solved(board):
    if curr_coord in solved_pieces:
        if forward:
            curr_coord = move_forward(curr_coord)
        else:
            board_idx[curr_coord[0]][curr_coord[1]] = 0
            curr_coord = move_back(curr_coord)
            board_idx[curr_coord[0]][curr_coord[1]] += 1
        continue

    valid = valid_nums(curr_coord[0], curr_coord[1], board)
    if len(valid[board_idx[curr_coord[0]][curr_coord[1]]:len(valid)]) > 0:
        forward = True
        board[curr_coord[0]][curr_coord[1]] = valid[board_idx[curr_coord[0]][curr_coord[1]]:len(valid)][0]
        curr_coord = move_forward(curr_coord)

    else:
        forward = False
        board[curr_coord[0]][curr_coord[1]] = 0
        board_idx[curr_coord[0]][curr_coord[1]] = 0
        if curr_coord[1] > 0:
            board_idx[curr_coord[0]][curr_coord[1] - 1] += 1
        else:
            board_idx[curr_coord[0] - 1][8] += 1
        curr_coord = move_back(curr_coord)

for i in board:
    print(i)

print(f"Time took: {time.time() - start}s")
