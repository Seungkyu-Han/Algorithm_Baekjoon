import sys

num = int(sys.stdin.readline())

result = {num}

cnt = 1
while 1 not in result:
    tmp = set()
    for i in result:
        if i % 3 == 0:
            tmp.add(i//3)
        if i % 2 == 0:
            tmp.add(i//2)
        tmp.add(i - 1)
    cnt += 1
    result = tmp

print(cnt - 1)
