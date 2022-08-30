from collections import deque
import sys

K = int(sys.stdin.readline())

W, H = map(int, sys.stdin.readline().split())

board = []

for i in range(H):
    board.append(list(map(int, sys.stdin.readline().split())))


visited = [[[1e9] * W for i in range(H)] for t in range(K + 1)]
for i in range(K + 1):
    visited[i][0][0] = 0


need_visit = deque()
need_visit.append((K, 0, 0, 0))  # chance, x, y, cnt

while need_visit:

    chance, x, y, cnt = need_visit.popleft()

    if chance > 0:
        go_list = [(x - 2, y - 1), (x - 1, y - 2), (x + 2, y - 1), (x + 1, y - 2), (x - 2, y + 1), (x - 1, y + 2), (x + 1, y + 2), (x + 2, y + 1)]
        for x_ptr, y_ptr in go_list:
            if 0 <= x_ptr < H and 0 <= y_ptr < W and board[x_ptr][y_ptr] == 0 and visited[chance-1][x_ptr][y_ptr] > cnt + 1:
                visited[chance-1][x_ptr][y_ptr] = cnt + 1
                need_visit.append((chance - 1, x_ptr, y_ptr, cnt + 1))

    for x_ptr, y_ptr in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= x_ptr < H and 0 <= y_ptr < W and board[x_ptr][y_ptr] == 0 and visited[chance][x_ptr][y_ptr] > cnt + 1:
            visited[chance][x_ptr][y_ptr] = cnt + 1
            need_visit.append((chance, x_ptr, y_ptr, cnt + 1))

result = 1e9

for i in range(K + 1):
    result = min(result, visited[i][-1][-1])

if result == 1e9:
    print(-1)
else:
    print(result)
