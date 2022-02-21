list1 = list(map(int, input().split()))

list1.sort()

a = abs(list1[3] + list1[0] -list1[1] - list1[2])
b = abs(list1[2] + list1[0] -list1[3] - list1[1])

print(min(a, b))
