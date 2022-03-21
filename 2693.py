num = int(input())

for i in range(num):
    list1 = list(map(int, input().split()))
    list1.sort(reverse=True)
    print(list1[2])
