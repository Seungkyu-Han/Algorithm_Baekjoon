import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

list1 = [i for i in range(M, N+1)]
list2 = list(list1)
for x in list1:
    for t in range(2, x):
        if x % t == 0:
            list2.remove(x)
            break

if 1 in list2:
    list2.remove(1)

if len(list2) == 0:
    print(-1)
else:
    print("%d\n%d" %(sum(list2), min(list2)))
