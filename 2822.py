list1 = [0 for i in range(8)]

for i in range(8):
    list1[i] = int(input())

list2 = sorted(list1, reverse=True)

list3 = [0 for i in range(5)]

total = 0
for i in range(5):
    total += list2[i]
    list3[i] = list1.index(list2[i])

list3.sort()

print(total)

for i in range(5):
    print(list3[i] + 1, end=' ')
