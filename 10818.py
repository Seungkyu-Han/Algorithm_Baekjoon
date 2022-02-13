import sys

num = int(input())
list1 = list(map(int, sys.stdin.readline().split()))

print("%d %d" % (min(list1), max(list1)))
