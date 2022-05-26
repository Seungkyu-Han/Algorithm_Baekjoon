import sys

num = int(sys.stdin.readline())

paper = [list(map(int, sys.stdin.readline().split())) for i in range(num)]

minus_one = 0
zero = 0
one = 0


def mypaper(x, y, n):
    global minus_one, zero, one

    num_check = paper[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if paper[i][j] != num_check:
                for k in range(3):
                    for t in range(3):
                        mypaper(x + k * n // 3, y + t * n // 3, n // 3)
                return
    if num_check == -1:
        minus_one += 1
    elif num_check == 0:
        zero += 1
    else:
        one += 1


mypaper(0, 0, num)
print(minus_one)
print(zero)
print(one)
