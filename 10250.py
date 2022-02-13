import math

T=int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if N%H==0:
        f = H
    else :
        f = N%H
    if (math.ceil(N/H))>=10:
        print("%d%d" %(f,math.ceil(N/H)))
    else:
        print("%d0%d" %(f,math.ceil(N/H)))
