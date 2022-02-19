num = int(input())
list1 = []

for _ in range(num):
    a, b = map(int, input().split())
    list1.append([b, a])

list1.sort()

for t in list1:
    print(t[1], t[0])
