def wood(lista, n, height):
    total = 0
    for i in range(n):
        if lista[i] - height > 0:
            total += lista[i] - height

    return total


N, M = map(int, input().split())

list1 = list(map(int, input().split()))

left, right = 0, max(list1)

while left <= right:
    mid = (left + right) // 2
    mywood = wood(list1, N, mid)

    if mywood >= M:
        left = mid + 1
    else:
        right = mid - 1

print(right)
