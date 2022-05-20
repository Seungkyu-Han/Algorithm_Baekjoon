from collections import deque

N, K = map(int, input().split())

time = 0
location = {N}
visited = [True for i in range(100001)]
visited[N] = False

while visited[K]:
    tmp = deque()

    for i in location:
        for t in (i - 1, i + 1, i * 2):
            if 0 <= t <= 100000 and visited[t]:
                visited[t] = False
                tmp.append(t)
    location = set(tmp)
    time += 1

print(time)
