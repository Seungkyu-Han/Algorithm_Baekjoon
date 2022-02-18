list1 = [9, 7, 8, 0, 9, 2, 1, 4, 1, 8]

for i in range(3):
    list1.append(int(input()))


total = 0

for i in range(len(list1)):
    if i % 2 == 0:
        total += list1[i]
    else:
        total += list1[i] * 3

print('The 1-3-sum is {} ' .format(total))
