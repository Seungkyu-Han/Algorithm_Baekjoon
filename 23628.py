import sys

S = list(map(int, sys.stdin.readline().split()))
E = list(map(int, sys.stdin.readline().split()))

days = (E[0] - S[0]) * 360 + (E[1] - S[1]) * 30 + (E[2] - S[2])
yea = days//360
wal_cha = yea * 12 if yea * 12 <= 36 else 36
yea = days//360
yun_cha = 0
plus = 15
for i in range(1, yea + 1):
    if i >= 3 and i % 2 == 1:
        plus += 1
    yun_cha += plus
print("{} {}" .format(yun_cha, wal_cha))
print("{}days" .format(days))
