L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

result = 0

if A/C >= B/D:
    result = (A//C if A/C == A//C else A//C+1)
else:
    result = (B//D if B/D == B//D else B//D+1)

print(L-result)
