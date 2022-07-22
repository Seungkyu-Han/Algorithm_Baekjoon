N = int(input())

result = [0] * (N + 1)
result[0] = 1

for i in range(2, N + 1, 2):
    tmp = result[i-2] * 3
    for t in range(0, i - 2, 2):
        tmp += (result[t] * 2)
    result[i] = tmp

print(result[N])
