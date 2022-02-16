N, M = map(int, input().split())

list1 = list(map(int, input().split()))
list1 = sorted(list1)

result = 0

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if result < list1[a]+list1[b]+list1[c] <= M:
                result = list1[a]+list1[b]+list1[c]


print(result)
