def mylist(n):
    list1 = []
    while n > 0:
        list1.append(n % 10)
        n //= 10
    return list1


def forres(n, list1):
    multi1 = 1
    multi2 = 1
    for i in range(n + 1):
        multi1 *= list1[i]

    for i in range(n + 1, len(list1)):
        multi2 *= list1[i]

    return multi1 == multi2


listx = mylist(int(input()))
ans = False

for i in range(len(listx) - 1):
    ans += forres(i, listx)

if ans:
    print('YES')
else:
    print('NO')
