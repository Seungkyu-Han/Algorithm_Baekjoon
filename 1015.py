import sys

cnt = int(sys.stdin.readline())
ans = list(map(int, sys.stdin.readline().split()))

result = sorted(ans)

restr = ''
for i in ans:
    index = result.index(i)
    restr += str(index) + ' '
    result[index] = 0

print(restr)
