import sys

s = sys.stdin.readline().rstrip()


if len(s) < 5:
    print('not cute')
elif s[len(s)-5:] == 'driip':
    print('cute')
else:
    print('not cute')
