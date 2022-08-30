import sys

N = int(sys.stdin.readline())

board = []
left_down = [[] for i in range(2 * N - 1)]
odd_max = 0
even_max = 0

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

for i in range(N):
    for t in range(N):
        if board[i][t] == 1:
            left_down[i + t].append((i, t))


def solve(cur_cnt, avoid, n):
    global odd_max, even_max

    if n >= 2 * N - 1:
        if n % 2 == 0:
            even_max = max(even_max, cur_cnt)
        else:
            odd_max = max(odd_max, cur_cnt)
        return

    for next in left_down[n]:
        for_x = next[0]
        for_y = N - next[1] - 1
        if avoid[for_x + for_y]:
            avoid[for_x + for_y] = False
            solve(cur_cnt + 1, avoid, n + 2)
            avoid[for_x + for_y] = True
    solve(cur_cnt, avoid, n + 2)


solve(0, [True] * (2 * N - 1), 0)
solve(0, [True] * (2 * N - 1), 1)

print(even_max + odd_max)
