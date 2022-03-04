n, m = map(int, input().split())

list1 = [i for i in range(2, n + 1)]
cnt = 0
result = 0

while cnt != m:
    num1 = list1.pop(0)
    cnt += 1
    if cnt == m:
        result = num1
        break
    for i in list1:
        if i % num1 == 0:
            cnt += 1
            if cnt == m:
                result = i
                break
            list1.remove(i)

print(result)
