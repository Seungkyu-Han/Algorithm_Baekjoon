import sys

N, M = map(int, sys.stdin.readline().split())

board = []
result = [[-1] * M for i in range(N)]
result[-1][-1] = 1

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


def solve(cur_n, cur_m):
    if result[cur_n][cur_m] != -1:
        return result[cur_n][cur_m]

    res = 0

    for x_ptr, y_ptr in ((cur_n - 1, cur_m), (cur_n + 1, cur_m), (cur_n, cur_m - 1), (cur_n, cur_m + 1)):
        if 0 <= x_ptr < N and 0 <= y_ptr < M and board[cur_n][cur_m] > board[x_ptr][y_ptr]:
            res += solve(x_ptr, y_ptr)

    result[cur_n][cur_m] = res
    return result[cur_n][cur_m]


solve(0, 0)
print(result[0][0])
