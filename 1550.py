str1 = input()
list1 = ['A', 'B', 'C', 'D', 'E', 'F']
total = 0

for i in range(len(str1)):
    if str1[i] in list1:
        total += (list1.index(str1[i]) + 10) * (16 ** (len(str1) - (i+1)))
    else:
        total += int(str1[i]) * (16 ** (len(str1) - (i+1)))

print(total)
