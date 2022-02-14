import sys

N = int(input())

stu_list = list(map(int, sys.stdin.readline().split()))

X, Y = map(int, sys.stdin.readline().split())

X_cnt = N * X // 100

Y_cnt = 0

for i in stu_list:
    if i >= Y:
        Y_cnt += 1

print("{} {}" .format(X_cnt, Y_cnt))
