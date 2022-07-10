import sys

doku = []

for i in range(9):
    doku.append(list(map(int, sys.stdin.readline().strip())))


def judge(cur_x, cur_y):
    for index in range(9):
        if index != cur_x and doku[cur_x][cur_y] == doku[index][cur_y]:
            return False

    for index in range(9):
        if index != cur_y and doku[cur_x][cur_y] == doku[cur_x][index]:
            return False

    plus_x = (cur_x // 3) * 3
    plus_y = (cur_y // 3) * 3

    for q in range(3):
        for w in range(3):
            if cur_x == plus_x + q and cur_y == plus_y + w:
                continue
            else:
                if doku[cur_x][cur_y] == doku[plus_x + q][plus_y + w]:
                    return False
    return True


def solve(num):
    if num == 81:
        for i in doku:
            print("".join(map(str, i)))
        exit(0)

    if doku[num // 9][num % 9] != 0:
        solve(num + 1)
    else:
        for index in range(1, 10):
            doku[num // 9][num % 9] = index
            if judge(num // 9, num % 9):
                solve(num + 1)
            doku[num // 9][num % 9] = 0

solve(0)
