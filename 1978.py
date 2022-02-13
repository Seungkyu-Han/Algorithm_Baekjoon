import sys

N = int(input())

list1 = list(map(int, sys.stdin.readline().split()))
cnt = 0

for i in list1:
    count = 1
    for x in range(2, i):
        count *= i % x
    if count != 0:
        cnt += 1

print(cnt - list1.count(1))
