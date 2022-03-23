n = int(input())
m = int(input())

n = (n // 100) * 100

while n % m != 0:
    n += 1

print("{0:0>2}" .format(n % 100))
