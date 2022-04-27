num = int(input())

cnt = 1
result = {num, }

while cnt < 5:
    tmp = set()
    for i in result:
        start = 1
        while i >= start ** 2:
            tmp.add(i - start ** 2)
            start += 1
    if 0 in tmp:
        break
    result = tmp
    cnt += 1

print(cnt)
