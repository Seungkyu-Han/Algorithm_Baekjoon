import sys

N = int(sys.stdin.readline())
limit = int(sys.stdin.readline())
ans = sys.stdin.readline().strip()

cnt = 0
total = 0
index = 0

while index < limit - 1:
    if ans[index] == 'O':
        cnt = 0
        index += 1
    else:
        if cnt >= N:
            total += 1
        if ans[index+1] == 'O':
            cnt += 1
            index += 2
        else:
            index += 1
            cnt = 0
print(total)
