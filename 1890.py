import sys

N = int(sys.stdin.readline())

pan = []

for i in range(N):
    pan.append(list(map(int, sys.stdin.readline().split())))

result = [[0] * N for i in range(N)]
result[0][0] = 1


def way(cur_x, cur_y):
    global result
    jump = pan[cur_x][cur_y]
    if cur_x + jump < N:
        result[cur_x + jump][cur_y] += result[cur_x][cur_y]
    if cur_y + jump < N:
        result[cur_x][cur_y + jump] += result[cur_x][cur_y]


for i in range(N):
    for t in range(N):
        if result[i][t] != 0:
            if i == N - 1 and t == N - 1:
                continue
            way(i, t)


print(result[-1][-1])
