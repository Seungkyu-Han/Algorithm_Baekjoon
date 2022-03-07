def gcd(n1, n2):
    while n2 != 0:
        r = n1 % n2
        n1 = n2
        n2 = r
    return n1


num = int(input())

for i in range(num):
    a, b = map(int, input().split())
    if b > a:
        a, b = b, a
    print((b * a)//(gcd(a, b)), gcd(a, b))
    
