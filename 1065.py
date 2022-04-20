num = int(input())

total = 0 if num != 1000 else -1

while num > 0:
    tmp = num
    numlist = []
    while tmp > 0:
        numlist.append(tmp % 10)
        tmp //= 10
    if len(numlist) < 3:
        total += 1
    elif numlist[2] - numlist[1] == numlist[1] - numlist[0]:
        total += 1
    num -= 1

print(total)
