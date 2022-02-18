import sys


def top(lists):
    if len(lists) == 0:
        print(-1)
    else:
        print(lists[len(lists)-1])


num = int(input())
list1 = []
for i in range(num):
    input_str = list(map(str, sys.stdin.readline().split()))
    if input_str[0] == 'push':
        list1.append(int(input_str[1]))
    elif input_str[0] == 'pop':
        print(list1.pop() if len(list1) != 0 else -1)
    elif input_str[0] == 'size':
        print(len(list1))
    elif input_str[0] == 'empty':
        if len(list1) == 0:
            print(1)
        else:
            print(0)
    else:
        top(list1)
