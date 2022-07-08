import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()
len_bomb = len(bomb)
last = bomb[-1]
stack = []

for i in string:
    stack.append(i)
    if i == last and ''.join(stack[-len_bomb:]) == bomb:
        del stack[-len_bomb:]

if stack:
    print(''.join(stack))
else:
    print('FRULA')
