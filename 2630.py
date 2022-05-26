num = int(input())

paper = []

for i in range(num):
    paper.append(list(map(int, input().split())))

white = 0
blue = 0


def mypaper(x, y, n):
    global white, blue
    tmp = paper[x][y]
    for t in range(x, x + n):
        for j in range(y, y + n):
            if tmp != paper[t][j]:
                mypaper(x, y, n//2)
                mypaper(x, y + n // 2, n // 2)
                mypaper(x + n // 2, y, n // 2)
                mypaper(x + n // 2, y + n // 2, n // 2)
                return
    if tmp == 0:
        white += 1
        return
    else:
        blue += 1
        return


mypaper(0, 0, num)
print(white)
print(blue)
