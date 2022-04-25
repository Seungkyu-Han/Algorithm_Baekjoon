import sys


def getlength(list1, list2):
    a = (list1[0] - list2[0]) ** 2
    b = (list1[1] - list2[1]) ** 2
    return a + b


num = int(input())

for i in range(num):
    dot = []
    for t in range(4):
        dot.append(list(map(int, sys.stdin.readline().split())))
    length = [getlength(dot[0], dot[1]), getlength(dot[0], dot[2]), getlength(dot[0], dot[3]),
              getlength(dot[1], dot[2]), getlength(dot[1], dot[3]), getlength(dot[2], dot[3])]
    result = set(length)
    if len(result) == 2:
        print(1)
    else:
        print(0)
