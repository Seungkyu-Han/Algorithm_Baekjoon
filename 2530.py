import sys

H, M, S = map(int, sys.stdin.readline().split())

plus = int(input())

S += plus % 60
plus = plus // 60
if S >= 60:
    S -= 60
    M += 1

M += plus % 60
plus = plus//60
if M >= 60:
    M -= 60
    H += 1

H += plus
H %= 24

print("{} {} {}" .format(H, M, S))
