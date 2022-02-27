import sys


def add_num(list_x, number):
    list_x[number-1] = True
    return list_x


def remove_num(list_x, number):
    list_x[number-1] = False
    return list_x


def check_num(list_x, number):
    if list_x[number-1]:
        print(1)
    else:
        print(0)


def toggle_num(list_x, number):
    if list_x[number-1]:
        list_x[number-1] = False
    else:
        list_x[number-1] = True
    return list_x


def all_num():
    list_x = [True for i in range(20)]
    return list_x


def empty():
    list_x = [False for i in range(20)]
    return list_x


num = int(input())

list1 = [False for i in range(20)]

for i in range(num):
    str1 = list(map(str, sys.stdin.readline().split()))
    if str1[0] == 'add':
        list1 = add_num(list1, int(str1[1]))
    elif str1[0] == 'remove':
        list1 = remove_num(list1, int(str1[1]))
    elif str1[0] == 'check':
        check_num(list1, int(str1[1]))
    elif str1[0] == 'toggle':
        list1 = toggle_num(list1, int(str1[1]))
    elif str1[0] == 'all':
        list1 = all_num()
    else:
        list1 = empty()
