def printfunc(list1, num):
    mylist = list(list1)
    count = 0
    while True:
        if mylist[0] == max(mylist):
            if num == 0:
                count += 1
                return count
            else:
                count += 1
                mylist.pop(0)
                num -= 1
        else:
            if num == 0:
                num = len(mylist) - 1
            else:
                num -= 1
            mylist.append(mylist.pop(0))


n = int(input())

for i in range(n):
    N, M = map(int, input().split())
    list_x = list(map(int, input().split()))
    print(printfunc(list_x, M))
