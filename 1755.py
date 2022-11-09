import sys

n, m = map(int, sys.stdin.readline().split())

nums = [str(i) for i in range(n, m + 1)]

result = []

for i in [8, 5, 4, 9, 1, 7, 6, 3, 2, 0]:
    tmp = []
    for t in nums:
        if t[0] == str(i) and len(t) == 1:
            result.append(t)
        elif t[0] == str(i):
            tmp.append(t)
        
    for t in [8, 5, 4, 9, 1, 7, 6, 3, 2, 0]:
        for k in tmp:
            if k[1] == str(t):
                result.append(k)

for i in range(len(result)):
    print(result[i], end = ' ')
    if i % 10 == 9:
        print()
