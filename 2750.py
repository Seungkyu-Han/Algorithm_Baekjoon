num = int(input())

list1 = [0 for i in range(num)]

for i in range(num):
    list1[i] = int(input())

list1.sort()

for i in list1:
    print(i)
