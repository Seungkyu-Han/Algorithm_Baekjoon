num = int(input())

list1 = []

for i in range(num):
    list1.append(list(map(int, input().split())))

list1.sort()

for k in list1:
    print('{} {}' .format(k[0], k[1]))
