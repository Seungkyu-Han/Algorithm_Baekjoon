import sys

cnt = int(input())
score = list(map(int, sys.stdin.readline().split()))
total = 0.0
for i in range(cnt):
    total += score[i]
print(total/cnt/max(score)*100)
