def mysort(str_x):
    total = 0
    for i in str_x:
        if i.isdecimal():
            total += int(i)
    return total


num = int(input())

list1 = [[i, "hey"] for i in range(num)]

for i in range(num):
    str1 = input()
    list1[i] = [len(str1), mysort(str1), str1]

list1.sort()


for i in list1:
    print(i[2])
