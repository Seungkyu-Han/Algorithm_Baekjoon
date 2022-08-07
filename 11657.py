import sys

N, M = map(int, sys.stdin.readline().split())

edges = []

for i in range(M):
    edges.append(list(map(int, sys.stdin.readline().split())))

distance = [float('inf')] * (N + 1)
distance[1] = 0


def solve():
    for q in range(N - 1):
        for start, end, weight in edges:
            if distance[end] > distance[start] + weight:
                distance[end] = distance[start] + weight

    tmp = list(distance)

    for start, end, weight in edges:
        if distance[end] > distance[start] + weight:
            distance[end] = distance[start] + weight

    for q in range(2, N):
        if tmp[q] != distance[q]:
            return False
    return True


if solve():
    for i in distance[2:]:
        if i == float('inf'):
            print(-1)
        else:
            print(i)
else:
    print(-1)
