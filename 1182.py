import sys

N, S = map(int, (sys.stdin.readline()).split())

ans = list(map(int, (sys.stdin.readline()).split()))

result = [0, ]

while ans:
    tmp = []
    for i in result:
        tmp.append(i + ans[-1])
        tmp.append(i)
    ans.pop()
    result = tmp
result.pop()

print(result.count(S))
