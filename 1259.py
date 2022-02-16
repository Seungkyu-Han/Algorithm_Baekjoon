while True:
    num = input()
    if int(num) == 0:
        break
    cnt = 0
    for i in range(len(num)//2):
        if num[i] == num[len(num)-i-1]:
            pass
        else:
            cnt += 1
    if cnt == 0:
        print('yes')
    else:
        print('no')
