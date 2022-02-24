num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    elif a % 10 == 1:
        print(1)
    elif a % 10 == 2:
        list1 = [6, 2, 4, 8]
        print(list1[b % 4])
    elif a % 10 == 3:
        list1 = [1, 3, 9, 7]
        print(list1[b % 4])
    elif a % 10 == 4:
        list1 = [6, 4]
        print(list1[b % 2])
    elif a % 10 == 5:
        print(5)
    elif a % 10 == 6:
        print(6)
    elif a % 10 == 7:
        list1 = [1, 7, 9, 3]
        print(list1[b % 4])
    elif a % 10 == 8:
        list1 = [6, 8, 4, 2]
        print(list1[b % 4])
    elif a % 10 == 9:
        list1 = [1, 9]
        print(list1[b % 2])
