import math

a, b, c = map(int, input().split())

print(math.ceil(a/c)*math.ceil(b/c))
