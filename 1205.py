import sys

N, new_score, P = map(int, sys.stdin.readline().split())

cur_score = []

if N > 0:
    cur_score = list(map(int, sys.stdin.readline().split()))

cnt = 1
same = 0

for i in cur_score:
    if i < new_score:
        break
    elif i == new_score:
        same += 1
        cnt += 1
    else:
        cnt += 1

if cnt <= P:
    print(cnt - same)
else:
    print(-1)
