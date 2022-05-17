import sys

cnt = int(input())

ans = [[0, 0] for i in range(cnt)]
total = 0

for i in range(cnt):
    start, end = map(int, sys.stdin.readline().split())
    ans[i] = [start, end]

ans = sorted(ans, key=lambda a: a[0])
ans = sorted(ans, key=lambda a: a[1])

prev = 0
total = 0

for start, end in ans:
    if start >= prev:
        total += 1
        prev = end

print(total)
