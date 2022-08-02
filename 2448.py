n = int(input())

k = 5
tmp = n // 3
cnt = 1

while tmp > 1:
    k = k * 2 + 1
    cnt += 1
    tmp //= 2

result = [[' '] * k for i in range(n)]


def solve(cur_x, cur_y, cur_cnt):
    global result
    if cur_cnt == 0:
        result[cur_x][cur_y] = '*'
        result[cur_x + 1][cur_y - 1] = '*'
        result[cur_x + 1][cur_y + 1] = '*'
        result[cur_x + 2][cur_y - 2] = '*'
        result[cur_x + 2][cur_y - 1] = '*'
        result[cur_x + 2][cur_y] = '*'
        result[cur_x + 2][cur_y + 1] = '*'
        result[cur_x + 2][cur_y + 2] = '*'
        return

    solve(cur_x, cur_y, cur_cnt - 1)
    solve(cur_x + 2 ** (cur_cnt - 1) * 3, cur_y - 2 ** (cur_cnt - 1) * 3, cur_cnt - 1)
    solve(cur_x + 2 ** (cur_cnt - 1) * 3, cur_y + 2 ** (cur_cnt - 1) * 3, cur_cnt - 1)


solve(0, k//2, cnt - 1)

for i in result:
    print(''.join(i))
