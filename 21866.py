list1 = list(map(int, input().split()))
list2 = [100, 100, 200, 200, 300, 300, 400, 400, 500]

total = 0
cnt = 0

for i in range(len(list1)):
    if list1[i] > list2[i]:
        print('hacker')
        cnt += 1
        break
    else:
        total += list1[i]

if total >= 100 and cnt == 0:
    print('draw')
elif cnt == 0:
    print('none')
