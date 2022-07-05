T = int(input())

for i in range(T):
    N = int(input())
    left = 0
    right = 14142140000

    while left < right:
        mid = (left + right) // 2

        range1 = mid * (mid - 1) // 2
        range2 = (mid - 1) * (mid - 2) // 2
        if range2 <= N < range1:
            break
        elif range2 > N:
            right = mid - 1
        else:
            left = mid + 1
    print((left + right)//2 - 2)
