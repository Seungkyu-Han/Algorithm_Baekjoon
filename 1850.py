a, b = map(int, input().split())

if b > a:
    a, b = b, a

while b != 0:
    r = a % b
    a = b
    b = r


print('1' * a)
