num = int(input())


def fact(n):
    cnt = 1
    for i in range(1, n+1):
        cnt *= i
    return cnt


for _ in range(num):
    a, b = map(int, input().split())
    max_n = max(a, b)
    min_n = min(a, b)
    print(fact(max_n)//(fact(max_n-min_n) * fact(min_n)))
    
