from collections import deque
import sys

N = int(sys.stdin.readline())

miro = [0] + list(map(int, sys.stdin.readline().split()))

visited = [-1] * (N + 1)
visited[1] = 0

need_visit = deque()
need_visit.append(1)

while need_visit and visited[N] == -1:
    cur = need_visit.popleft()

    for i in range(miro[cur]):
        if (i + 1) + cur <= N and visited[i + 1 + cur] == -1:
            visited[i + 1 + cur] = visited[cur] + 1
            need_visit.append(i + 1 + cur)

print(visited[N])
