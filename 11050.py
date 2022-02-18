def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


N, K = map(int, input().split())

print(fact(N)//(fact(K)*fact(N-K)))
