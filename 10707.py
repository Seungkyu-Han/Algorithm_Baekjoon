A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = P * A
Y = B + (0 if P <= C else (P - C) * D)

print(min(X, Y))
