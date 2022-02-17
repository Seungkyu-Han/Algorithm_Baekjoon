a, b, c = map(int, input().split())

a -= 11
b -= 11
c -= 11
print(a*1440+b*60+c if a*1440+b*60+c >= 0 else -1)
