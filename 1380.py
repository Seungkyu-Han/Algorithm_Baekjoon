cnt = 1

while True:
    num = int(input())
    if num == 0:
        break
    list1 = ['name' for i in range(num)]
    list2 = [2 for i in range(num)]
    for i in range(num):
        list1[i] = input()
    for i in range(2 * num - 1):
        a, b = map(str, input().split())
        list2[int(a) - 1] -= 1

    print(cnt, list1[list2.index(1)])
    cnt += 1
    
