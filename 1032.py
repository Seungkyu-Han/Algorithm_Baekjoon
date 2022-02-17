num = int(input())

list1 = []

for i in range(num):
    list1.append(input())

result = list(list1[0])

for t in range(num):
    for k in range(len(list1[t])):
        if result[k] != list1[t][k]:
            result[k] = str('?')

print(''.join(result) + ' ')
