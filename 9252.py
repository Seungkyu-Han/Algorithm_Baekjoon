import sys

str1 = list(sys.stdin.readline().strip())
str2 = list(sys.stdin.readline().strip())

len_str1 = len(str1)
len_str2 = len(str2)

result = [[''] * (len_str2 + 1) for i in range(len_str1 + 1)]

for i in range(1, len_str1 + 1):
    for t in range(1, len_str2 + 1):
        if str1[i - 1] == str2[t - 1]:
            result[i][t] = result[i-1][t-1] + str1[i-1]
        else:
            if len(result[i-1][t]) > len(result[i][t-1]):
                result[i][t] = result[i-1][t]
            else:
                result[i][t] = result[i][t-1]

print(len(result[-1][-1]))
print(result[-1][-1])
