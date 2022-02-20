num = int(input())

list1 = list(map(int, input().split()))

list1.sort()

if num % 2 == 0:
    print(list1[0] * list1[num-1])
else:
    print(list1[num//2] ** 2)
