import sys

A, P = map(int, sys.stdin.readline().split())

target = 0
visited = [A]

while True:
    new = 0

    while A > 0:
        new += (A % 10) ** P
        A //= 10

    if new in visited:
        target = new
        break
    else:
        visited.append(new)
        A = new

print(visited.index(target))
