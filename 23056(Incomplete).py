N, M = map(int, input().split())

list1 = []
cnt_list = [0 for i in range(N)]
while True:
    ans = list(map(str, input().split()))
    if ans[0] == '0' and ans[1] == '0':
        break
    if cnt_list[int(ans[0])-1] >= M:
        continue
    else:
        ans.append(len(ans[1]))
        tmp = ans[1]
        ans[1] = ans[2]
        ans[2] = tmp
        list1.append(ans)
        cnt_list[int(ans[0])-1] += 1

list1 = sorted(list1)

for i in list1:
    if int(i[0]) % 2 == 1:
        print('{} {}' .format(i[0], i[2]))

for i in list1:
    if int(i[0]) % 2 == 0:
        print('{} {}' .format(i[0], i[2]))
