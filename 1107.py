num = int(input())
n = int(input())

if n:
    broken = set(map(str, input().split()))
else:
    broken = set()


cnt = abs(100-num)
for i in range(1000000):
    if not(set(str(i)) & broken):
        cnt = min(cnt, len(str(i)) + abs(i - num))

print(cnt)
