cases = int(input())

for i in range(cases):
    a,b = map(int, input().split())
    ans = a + b
    print("Case #%d: %d"%(i+1, ans ))
