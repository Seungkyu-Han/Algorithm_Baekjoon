import sys

num = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().strip().split()))

result = sorted(list(set(arr)))

mydict = {result[i]: i for i in range(len(result))}

for i in arr:
    print(mydict[i], end=' ')
