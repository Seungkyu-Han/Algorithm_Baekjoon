import sys

N = int(sys.stdin.readline())

total = 0
area = []

for i in range(N):
    area.append(tuple(map(int, sys.stdin.readline().split())))

area.append(area[0])

for i in range(N):
    total += (area[i][0] * area[i+1][1] - area[i+1][0] * area[i][1])

total /= 2

total = abs(total)

print("%.1f" % total)
