num = int(input())

list1 = []

for i in range(num):
    list1.append(input())

list1 = list(set(list1))

list2 = [[len(k), k] for k in list1]
list2.sort()

for t in list2:
    print(t[1])
