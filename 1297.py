a, b, c = map(int, input().split())
k = a/((b**2) + (c**2))**0.5
print(int(k * b), int(k * c))
