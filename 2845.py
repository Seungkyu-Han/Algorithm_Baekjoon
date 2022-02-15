L, P = map(int, input().split())

list1 = list(map(int, input().split()))

for i in range(len(list1)):
    list1[i] -= L * P

print("{} {} {} {} {}" .format(list1[0], list1[1], list1[2], list1[3], list1[4]))
