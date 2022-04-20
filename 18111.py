def minecraft(lista, height, block):
    mytime = 0
    curblock = block
    for t in lista:
        if t - height > 0:
            mytime += 2 * (t - height)
            curblock += (t - height)
        elif height - t > 0:
            mytime += (height - t)
            curblock -= (height - t)

    return mytime if curblock >= 0 else -1


N, M, B = map(int, input().split())

list1 = []

for i in range(N):
    list1 += list(map(int, input().split()))

resheight = 0
restime = minecraft(list1, 0, B)

for i in range(257):
    mytime = minecraft(list1, i, B)
    if mytime >= 0:
        if mytime < restime:
            restime = mytime
            resheight = i
        elif mytime == restime:
            resheight = i

print(restime, resheight)
