import sys

num = int(sys.stdin.readline())

for i in range(num):
    ans = sys.stdin.readline().strip()
    input()
    result = sys.stdin.readline().rstrip()[1:-1].split(',')
    rev = 1
    flag = 1
    if result == ['']:
        result = []
    for t in ans:
        if t == 'R':
            rev *= -1
        else:
            if len(result) < 1:
                flag *= 0
                continue
            if rev == 1:
                result.pop(0)
            else:
                result.pop()
    if flag == 0:
        print('error')
    else:
        if rev == -1:
            result.reverse()
        print("[" + ",".join(result) + "]")
