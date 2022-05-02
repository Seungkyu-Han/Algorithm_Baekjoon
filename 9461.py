result = [0] * 100

result[0] = 1
result[1] = 1
result[2] = 1
result[3] = 2
result[4] = 2
for i in range(5, 100):
    result[i] = result[i-1] + result[i-5]

num = int(input())

for t in range(num):
    ans = int(input())
    print(result[ans-1])
