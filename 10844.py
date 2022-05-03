num = int(input())

result = [1, 1, 2, 2, 2, 2, 2, 2, 2, 1]


for t in range(num - 2):
    tmp = [0 for i in range(10)]
    for i in range(10):
        if i == 0:
            tmp[0] = result[1]
        elif i == 9:
            tmp[9] = result[8]
        else:
            tmp[i] = result[i-1] + result[i+1]
    result = tmp


if num == 1:
    print(9)
elif num == 2:
    print(17)
else:
    print(sum(result) % 1000000000)
