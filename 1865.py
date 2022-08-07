import sys

for _ in range(int(sys.stdin.readline())):
    N, M, W = map(int, sys.stdin.readline().split())
    edges = []

    for i in range(M):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append([S, E, T])
        edges.append([E, S, T])

    for i in range(W):
        S, E, T = map(int, sys.stdin.readline().split())
        edges.append([S, E, -T])

    distance = [1e9] * (N + 1)
    distance[1] = 0

    def solve():
        for q in range(N):
            for start, end, weight in edges:
                dist = distance[start] + weight
                if dist < distance[end]:
                    distance[end] = dist
                    if q == N - 1:
                        return "YES"
        return "NO"

    print(solve())
