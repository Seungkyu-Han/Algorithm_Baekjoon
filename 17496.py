N, T, C, P = map(int, input().split())
if N % T == 0:
    N -= 1
print(P * C * (N//T))
