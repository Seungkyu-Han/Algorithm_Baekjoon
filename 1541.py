ans = input()


tmp = ""
result = []
for i in ans:
    if i.isnumeric():
        tmp += i
    else:
        result.append(int(tmp))
        tmp = ""
        result.append(i)
result.append(int(tmp))

total = 0
cnt = 0

for i in range(len(result), 0, -1):
    i -= 1
    if type(result[i]) is int:
        cnt += result[i]
    elif result[i] == '-':
        total -= cnt
        cnt = 0

total += cnt
print(total)
