import sys

def gogo(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return gogo(num - 1) + gogo(num - 2) + gogo(num - 3)


num = int(sys.stdin.readline())
for i in range(num):
    print(gogo(int(input())))
