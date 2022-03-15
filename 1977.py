import math

a = int(input())
b = int(input())

a1 = math.ceil(a ** 0.5)
b1 = math.floor(b ** 0.5)

num = []

if a1 == b1:
    if a == a1 ** 2:
        num.append(a1)
    elif b == b1 ** 2:
        num.append(b)
    else:
        pass
else:
    num = [i * i for i in range(a1, b1 + 1)]


if len(num) == 0:
    print(-1)
else:
    print(sum(num))
    print(num[0])
