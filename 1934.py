def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


num = int(input())

result = []

for i in range(num):
    a, b = map(int, input().split())
    result.append(int(a * b / gcd(a, b)))

for i in result:
    print(i)
