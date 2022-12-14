dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def rotation(puzzle):
    n = len(puzzle)
    m = len(puzzle[0])
    result = [[0] * n for _ in range(m)]
    for r in range(n):
        for c in range(m):
            result[c][n-1-r] = puzzle[r][c]

    return result


def bfs(i, j, table, check):
    puzzle = []
    n = len(table)
    q = [(i, j)]
    check[i][j] = True
    while q:
        x, y = q.pop()
        puzzle.append([x, y])
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not check[nx][ny] and table[nx][ny] == 1:
                q.append((nx, ny))
                check[nx][ny] = True

    return puzzle
def board_bfs(i, j, board, check):
    board_li = []
    n = len(board)
    q = [(i, j)]
    check[i][j] = True
    while q:
        x, y = q.pop()
        board_li.append([x, y])
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if not (0 <= nx < n and 0 <= ny < n):
                continue
            if not check[nx][ny] and board[nx][ny] == 0:
                q.append((nx, ny))
                check[nx][ny] = True

    return board_li


def trans_puzzle(puzzle_location):
    r_min, r_max = 100, -1
    c_min, c_max = 100, -1
    for location in puzzle_location:
        r, c = location
        r_min = min(r_min, r)
        r_max = max(r_max, r)
        c_min = min(c_min, c)
        c_max = max(c_max, c)

    r_len = r_max - r_min + 1
    c_len = c_max - c_min + 1
    trans = [[0] * c_len for _ in range(r_len)]
    for location in puzzle_location:
        x = location[0] - r_min
        y = location[1] - c_min
        trans[x][y] = 1

    return trans

def solution(game_board, table):
    n = len(game_board)
    answer = 0
    puzzles = []
    boards = []
    check = [[False] * n for _ in range(n)]
    board_check = [[False]* n for _ in range(n)]
    puzzle_sum = []
    board_sum = []
    puzzle_check = []
    boarder_check = []
    for i in range(n):
        for j in range(n):
            if table[i][j] == 1 and not check[i][j]:
                puzzle_location = bfs(i, j, table, check)
                puzzle = trans_puzzle(puzzle_location)
                puzzles.append(puzzle)
                puzzle_check.append(1)
                puzzle_sum.append(len(puzzle_location))
            if game_board[i][j] == 0 and not board_check[i][j]:
                board_location = board_bfs(i,j, game_board, board_check)
                board = trans_puzzle(board_location)
                boards.append(board)
                boarder_check.append(1)
                board_sum.append(len(board_location))

    for x in range(len(board_sum)):
        for y in range(len(puzzle_sum)):
            if board_sum[x] == puzzle_sum[y] and boarder_check[x] == 1 and puzzle_check[y] == 1:
                    a = puzzles[y]
                    b = rotation(a)
                    c = rotation(b)
                    d = rotation(c)
                    if boards[x]  == a:
                        boarder_check[x] = 0
                        puzzle_check[y] = 0
                        answer += puzzle_sum[y]
                    elif boards[x] == b:
                        boarder_check[x] = 0
                        puzzle_check[y] = 0
                        answer += puzzle_sum[y]
                    elif boards[x] == c:
                        boarder_check[x] = 0
                        puzzle_check[y] = 0
                        answer += puzzle_sum[y]
                    elif boards[x] == d:
                        boarder_check[x] = 0
                        puzzle_check[y] = 0
                        answer += puzzle_sum[y]

    return answer