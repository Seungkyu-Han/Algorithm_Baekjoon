import sys
import math

A, B, V = map(int, sys.stdin.readline().split())

print(int(math.ceil(float(V-A)/float(A-B))+1))
