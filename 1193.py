x = int(input())

cnt = 1
rg = 0

while not(rg < x <= rg + cnt):
    rg += cnt
    cnt += 1

if cnt % 2 == 0:
    print("%d/%d" % (x-rg, cnt + 1 - x + rg))
else:
    print("%d/%d" % (cnt + 1 - x + rg, x-rg))
