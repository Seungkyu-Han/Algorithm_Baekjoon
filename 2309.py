import sys

height = []

for i in range(9):
    height.append(int(sys.stdin.readline()))

total = sum(height)


def solve():
    for q in range(9):
        for w in range(q + 1, 9):

            if total - height[q] - height[w] == 100:
                for t in sorted(height):
                    if t == height[q] or t == height[w]:
                        continue
                    print(t)
                return

solve()
