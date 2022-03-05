num = int(input())

list1 = [" " for i in range(num)]

for i in range(num):
    list1[i] = input()

list2 = []

while len(list1) != 0:
    list2.append([list1.count(list1[0]), list1[0]])
    list1.remove(list1[0])

list2.sort(reverse=True)

while True:
    if len(list2) > 1 and list2[0][0] == list2[1][0]:
        del list2[0]
    else:
        print(list2[0][1])
        break
