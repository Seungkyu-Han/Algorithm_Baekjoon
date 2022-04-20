N, K = map(int, input().split())

list1 = []

for i in range(N):
    list1.append(int(input()))

total = 0
cnt = N - 1

while K > 0:
    total += (K // list1[cnt])
    K %= list1[cnt]
    cnt -= 1

print(total)
