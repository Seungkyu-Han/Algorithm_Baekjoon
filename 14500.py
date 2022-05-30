import sys

N, M = map(int, sys.stdin.readline().split())

value = []
for i in range(N):
    value.append(list(map(int, sys.stdin.readline().split())))

TT = (
    ((0, 1), (0, 2), (0, 3)),
    ((1, 0), (2, 0), (3, 0)),
    ((0, 1), (1, 0), (1, 1)),
    ((1, 0), (2, 0), (2, 1)),
    ((1, 0), (2, 0), (2, -1)),
    ((0, -1), (1, 0), (2, 0)),
    ((0, 1), (1, 0), (2, 0)),
    ((1, 0), (1, 1), (1, 2)),
    ((0, 1), (0, 2), (-1, 2)),
    ((0, 1), (0, 2), (1, 2)),
    ((0, 1), (0, 2), (1, 0)),
    ((1, 0), (0, 1), (-1, 1)),
    ((1, 0), (1, 1), (2, 1)),
    ((0, 1), (-1, 1), (-1, 2)),
    ((0, 1), (1, 1), (1, 2)),
    ((0, 1), (1, 1), (0, 2)),
    ((0, 1), (-1, 1), (0, 2)),
    ((-1, 0), (-1, -1), (-2, 0)),
    ((-1, 0), (-1, 1), (-2, 0)),
)

result = 0

for i in range(N):
    for t in range(M):
        for fi, se, th in TT:
            fi_N, fi_M = fi
            se_N, se_M = se
            th_N, th_M = th
            if 0 <= fi_N + i < N and 0 <= se_N + i < N and 0 <= th_N + i < N and 0 <= fi_M + t < M and 0 <= se_M + t < M and 0 <= th_M + t < M:
                result = max(result, value[i][t] + value[i + fi_N][t + fi_M] + value[i + se_N][t + se_M] + value[i + th_N][t + th_M])

print(result)
