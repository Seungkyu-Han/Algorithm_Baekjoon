num = int(input())

list1 = list(map(int, input().split()))

list1.sort(reverse=True)

list2 = list(map(int, input().split()))

list2.sort()

total = 0

for k in range(num):
    total += list1[k] * list2[k]

print(total)
