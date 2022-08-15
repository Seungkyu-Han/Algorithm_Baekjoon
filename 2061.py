import sys

K, L = map(int, sys.stdin.readline().split())

cur = 2

while K % cur != 0 and cur < L:
    cur += 1

if cur >= L:
    print('GOOD')
else:
    print('BAD', cur)
