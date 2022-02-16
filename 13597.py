N, M = map(int, input().split())

if N == M:
    print(N)
else:
    print(N if N >= M else M)
