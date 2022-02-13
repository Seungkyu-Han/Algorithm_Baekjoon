import sys

listX = []
listY = []

for i in range(3):
    a, b = map(int, sys.stdin.readline().split())
    listX.append(a)
    listY.append(b)

listX.sort()
listY.sort()

x = int(listX[1])
y = int(listY[1])

listX.remove(x)
listY.remove(y)
listX.remove(x)
listY.remove(y)

print("%d %d" % (listX[0], listY[0]))
