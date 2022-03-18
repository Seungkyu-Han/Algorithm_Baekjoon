import math

n, m = map(int, input().split())

list1 = [0 for i in range(m)]
list2 = [0 for i in range(m)]

for i in range(m):
    list1[i], list2[i] = map(int, input().split())


case1 = min(list1) * math.ceil(n / 6)
case2 = min(list1) * (n // 6) + min(list2) * (n % 6)
case3 = min(list2) * n

print(min(case1, case2, case3))
