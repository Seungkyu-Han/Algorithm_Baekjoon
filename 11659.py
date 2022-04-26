import sys

N, M = map(int, sys.stdin.readline().split())

ans = list(map(int, sys.stdin.readline().split()))
calc = [0 for i in range(N)]
calc[0] = ans[0]
for i in range(1, N):
    calc[i] = calc[i - 1] + ans[i]
calc.insert(0, 0)
result = []


for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    result.append(calc[b] - calc[a - 1])

for i in result:
    print(i)
