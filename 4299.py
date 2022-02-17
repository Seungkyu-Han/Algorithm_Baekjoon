n, m = map(int, input().split())

a = (n+m)//2
b = (n-m)//2

if n + m < 0 or n - m < 0 or (n + m) % 2:
    print(-1)
elif a >= b:
    print(a, b)
else:
    print(b, a)
