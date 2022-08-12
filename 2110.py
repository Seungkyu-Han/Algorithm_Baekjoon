import sys

N, M = map(int, sys.stdin.readline().split())

house = []

for i in range(N):
    house.append(int(sys.stdin.readline()))

house.sort()

start = 1
end = house[-1]
result = 0

while start <= end:
    mid = (start + end) // 2
    cur = house[0]
    cnt = 1

    for i in range(1, N):
        if house[i] >= cur + mid:
            cnt += 1
            cur = house[i]

    if cnt >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
