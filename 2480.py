list1 = list(map(int, input().split()))

list1 = sorted(list1)

if list1[0] == list1[2]:
    print(10000 + list1[0] * 1000)
elif list1[0] == list1[1] or list1[1] == list1[2]:
    print(1000 + list1[1] * 100)
else:
    print(list1[2] * 100)
