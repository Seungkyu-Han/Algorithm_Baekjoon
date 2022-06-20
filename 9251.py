str1 = input()
str2 = input()

result = [[0] * (len(str2) + 1) for i in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for t in range(1, len(str2) + 1):
        if str1[i-1] == str2[t-1]:
            result[i][t] = result[i-1][t-1] + 1
        else:
            result[i][t] = max(result[i-1][t], result[i][t-1])


print(result[-1][-1])
