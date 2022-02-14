H, M = map(int, input().split())
plus = int(input())

H += plus // 60
M += plus % 60

if M >= 60:
    M -= 60
    H += 1

print("{} {}" .format(H % 24, M))

