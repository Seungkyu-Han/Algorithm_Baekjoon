import sys

num = int(sys.stdin.readline())

score = [0] * num

for i in range(num):
    score[i] = list(map(int, sys.stdin.readline().split()))

total = [score[0][0]]

for i in range(1, num):
    tmp = []
    for t in range(i + 1):
        if t == 0:
            tmp.append(total[0] + score[i][0])
        elif t == i:
            tmp.append(total[-1] + score[i][-1])
        else:
            tmp.append(max(total[t-1], total[t]) + score[i][t])
    total = tmp

print(max(total))
