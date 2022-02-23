num = int(input())

for i in range(num):
    cnt = input()
    reversed_cnt = cnt[::-1]
    cnt = int(cnt) + int(reversed_cnt)
    list1 = list(str(cnt))
    death = 0
    for t in range(len(list1)//2):
        if list1[t] != list1[len(list1)-1-t]:
            death += 1

    if death == 0:
        print('YES')
    else:
        print('NO')
