num = int(input())

list1 = []

for i in range(num):
    age, name = map(str, input().split())
    list1.append([int(age), i, name])

list1.sort()

for k in list1:
    print(k[0], k[2])
