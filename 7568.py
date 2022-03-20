num = int(input())

list1 = [list(map(int, input().split())) for i in range(num)]

for i in range(num):
    rank = 1
    for j in range(num):
        if list1[i][0] < list1[j][0] and list1[i][1] < list1[j][1]:
            rank += 1
    print(rank, end=' ')
