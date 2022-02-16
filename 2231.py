n = int(input())

result = 0

for i in range(1, n+1):
    num = i
    total = i
    while num != 0:
        total += num % 10
        num = num // 10
    if total == n:
        result = i
        break

print(result)
