num = int(input())

list1 = [0 for i in range(num)]
list2 = [0 for i in range(num)]
for i in range(num):
    list1[i] = int(input())

total = sum(list1) // 2
for i in range(1, num, 2):
    total -= list1[i]

list2[0] = total

for i in range(1, num):
    list2[i] = list1[i-1] - list2[i-1]

for i in list2:
    print(i)
