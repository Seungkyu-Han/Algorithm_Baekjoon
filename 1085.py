import sys

x, y, w, h = map(int, sys.stdin.readline().split())

rex = x if x <= w-x else w-x
rey = y if y <= h-y else h-y

print(rex if rex <= rey else rey)
