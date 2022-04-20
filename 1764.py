import sys

N, M = map(int, sys.stdin.readline().split())

set1 = set()
set2 = set()

for i in range(N):
    set1.add(sys.stdin.readline().strip())

for i in range(M):
    set2.add(sys.stdin.readline().strip())

result = sorted(list(set1 & set2))

print(len(result))

for i in result:
    print(i)
