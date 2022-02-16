list1 = [1, 1, 2, 2, 2, 8]
list2 = list(map(int, input().split()))

for i in range(6):
    print("%d" %(list1[i] - list2[i]), end=' ')
