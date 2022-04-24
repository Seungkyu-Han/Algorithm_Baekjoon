import sys

num = int(sys.stdin.readline())

for i in range(num):
    str1 = sys.stdin.readline().strip()
    left = []
    right = []

    for t in str1:
        if t == '>':
            if right:
                left.append(right.pop())
        elif t == '<':
            if left:
                right.append(left.pop())
        elif t == '-':
            if left:
                left.pop()
        else:
            left.append(t)

    result = ''.join(k for k in left + list(reversed(right)))
    print(result)
