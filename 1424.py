import sys

N = int(sys.stdin.readline())
L = int(sys.stdin.readline())
C = int(sys.stdin.readline())

each_cnt = (C + 1) // (L + 1)
res = 1e9

for i in range(each_cnt, 0, -1):
    if i % 13 == 0:
        continue

    tmp = N // i

    remain = N % i

    if remain > 0:
        if remain % 13 == 0 and remain + 1 == i:
            tmp += 2
        elif tmp == 0 and remain % 13 == 0:
            tmp += 2
        else:
            tmp += 1
    res = min(res, tmp)

print(res)
