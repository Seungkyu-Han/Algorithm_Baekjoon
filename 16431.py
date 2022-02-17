list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))
list3 = list(map(int, input().split()))

dist1 = max(abs(list3[0]-list1[0]), abs(list3[1]-list1[1]))
dist2 = abs(list3[0] - list2[0]) + abs(list3[1] - list2[1])

if dist1 == dist2:
    print('tie')
elif dist1 > dist2:
    print('daisy')
else:
    print('bessie')
