num = int(input())

for i in range(num):
    k = int(input())
    n = int(input())
    list1 = [i+1 for i in range(n)]
    list2 = list(list1)
    for x in range(1, k+1):
        for t in range(n):
            list2[t] = sum(list1[0:t+1])
        list1 = list(list2)
    print(list1[n-1])
