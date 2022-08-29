from collections import deque
import sys

game = [[0] * 501 for i in range(501)]

N = int(sys.stdin.readline())

for i in range(N):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    x1 = min(X1, X2)
    x2 = max(X1, X2)
    y1 = min(Y1, Y2)
    y2 = max(Y1, Y2)
    for t in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            game[t][k] = 1

N = int(sys.stdin.readline())

for i in range(N):
    X1, Y1, X2, Y2 = map(int, sys.stdin.readline().split())
    x1 = min(X1, X2)
    x2 = max(X1, X2)
    y1 = min(Y1, Y2)
    y2 = max(Y1, Y2)
    for t in range(x1, x2 + 1):
        for k in range(y1, y2 + 1):
            game[t][k] = 2

visited = [[True] * 501 for i in range(501)]
visited[0][0] = True

need_visit = deque()
need_visit.append((0, 0, 0))

result = 0
flag = False

while need_visit:

    cur_cnt, x, y = need_visit.popleft()

    if x == 500 and y == 500:
        flag = True
        result = cur_cnt
        break

    for x_ptr, y_ptr in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
        if 0 <= x_ptr < 501 and 0 <= y_ptr < 501 and visited[x_ptr][y_ptr]:
            if game[x_ptr][y_ptr] == 0:
                visited[x_ptr][y_ptr] = False
                need_visit.appendleft((cur_cnt, x_ptr, y_ptr))
            elif game[x_ptr][y_ptr] == 1:
                visited[x_ptr][y_ptr] = False
                need_visit.append((cur_cnt + 1, x_ptr, y_ptr))

if flag:
    print(result)
else:
    print(-1)
