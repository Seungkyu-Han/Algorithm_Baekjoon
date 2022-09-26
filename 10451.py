import sys

for _ in range(int(sys.stdin.readline())):
    N = int(sys.stdin.readline())
    graph = list(map(int, sys.stdin.readline().split()))
    result = 0

    visited = [False] * (N + 1)

    for i in range(1, N + 1):
        if visited[i]:
            continue

        next = i

        while not visited[next]:
            visited[next] = True
            next = graph[next - 1]

        result += 1

    print(result)
