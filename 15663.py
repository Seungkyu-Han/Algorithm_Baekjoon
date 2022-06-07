import sys

N, M = map(int, sys.stdin.readline().split())

num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort()

tmp = []
visited = [False] * N


def result(start, n, m):
    if len(tmp) == M:
        print(*tmp)
        return
    op = 0
    for i in range(n):
        if not visited[i] and op != num_list[i]:
            visited[i] = True
            tmp.append(num_list[i])
            op = num_list[i]
            result(start + 1, n, m)
            visited[i] = False
            tmp.pop()

result(0, N, M)
