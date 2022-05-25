from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())

ladder = dict()
snake = dict()

for i in range(N):
    start, end = map(int, sys.stdin.readline().split())
    ladder[start] = end

for i in range(M):
    start, end = map(int, sys.stdin.readline().split())
    snake[start] = end

need_visit = deque()
need_visit.append(1)
visited = [0] * 101

while visited[100] == 0:
    cur = need_visit.popleft()
    for i in range(1, 7):
        go = cur + i
        if go > 100 or visited[go] > 0:
            continue
        if go in ladder.keys():
            go = ladder[go]
        elif go in snake.keys():
            go = snake[go]
        if visited[go] > 0:
            continue
        visited[go] = visited[cur] + 1
        need_visit.append(go)

print(visited[100])
