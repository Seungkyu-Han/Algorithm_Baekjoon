num = int(input())
list1 = [0, 0]
for i in range(1, num + 1):
    two, five = i, i
    while two % 2 == 0:
        list1[0] += 1
        two //= 2
    while five % 5 == 0:
        list1[1] += 1
        five //= 5

print(min(list1))
