import sys

num = int(sys.stdin.readline())

for i in range(num):
    cnt = int(sys.stdin.readline())
    mydict = {}
    for t in range(cnt):
        name, cate = map(str, sys.stdin.readline().split())
        if cate in mydict:
            mydict[cate] = mydict.get(cate) + 1
        else:
            mydict[cate] = 1

    result = mydict.values()
    total = 1
    for k in result:
        total *= (k + 1)
    print(total - 1)
