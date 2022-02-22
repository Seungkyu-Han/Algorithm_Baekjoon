num = int(input())

for i in range(num):
    cnt = int(input())
    if str(cnt ** 2)[-(len(str(cnt))):] == str(cnt):
        print('YES')
    else:
        print('NO')
