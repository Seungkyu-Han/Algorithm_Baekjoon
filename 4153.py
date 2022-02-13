import sys

list1 = [1, 2, 3]

while True:
    list1[0], list1[1], list1[2] = map(int, sys.stdin.readline().split())
    list1.sort()
    if list1[0] == 0 and list1[1] == 0 and list1[2] == 0:
        break
    elif list1[0]**2 + list1[1]**2 == list1[2]**2:
        print('right')
    else:
        print('wrong')
