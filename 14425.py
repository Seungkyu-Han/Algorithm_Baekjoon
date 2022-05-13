import sys

N, M = map(int, input().split())

myset = list()

for i in range(N):
    myset.append(sys.stdin.readline().strip())

total = 0

for i in range(M):
    ans = sys.stdin.readline().strip()
    if ans in myset:
        total += 1
print(total)
