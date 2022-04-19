N, M = map(int, input().split())

pocketmon = {}
list1 = []

for i in range(N):
    pocketmon[i] = input()

for i in range(M):
    list1.append(input())

valueList = list(pocketmon.values())


for i in range(M):
    if list1[i].isnumeric():
        target = int(list1[i]) - 1
        print(pocketmon[target])
    else:
        print(valueList.index(list1[i]) + 1)
