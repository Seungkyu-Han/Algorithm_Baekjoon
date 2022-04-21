import sys

N, M = map(int, sys.stdin.readline().split())

passworddict = {}

for i in range(N):
    str1, str2 = map(str, sys.stdin.readline().strip().split())
    passworddict[str1] = str2

result = []

for i in range(M):
    str1 = sys.stdin.readline().strip()
    result.append(passworddict.get(str1))

for i in result:
    print(i)
