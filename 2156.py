import sys

num = int(sys.stdin.readline())

wine = []

for i in range(num):
    wine.append(int(sys.stdin.readline()))

wine.append(0)
wine.append(0)

result = [wine[0], wine[0] + wine[1], sum(wine[0:3]) - min(wine[0:3])]

for i in range(3, num):
    tmp = max(result[i - 2] + wine[i], result[i-3] + wine[i] + wine[i-1], result[i-1])
    result.append(tmp)

print(result[num-1])
