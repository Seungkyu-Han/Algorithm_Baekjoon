import sys

sys.setrecursionlimit(10 ** 6)
n = int(sys.stdin.readline())

in_ord = list(map(int, sys.stdin.readline().split()))
post_ord = list(map(int, sys.stdin.readline().split()))

indexes = [0] * (n + 1)

for i in range(n):
    indexes[in_ord[i]] = i


def solve(in_start, in_end, post_start, post_end):

    if in_start > in_end or post_start > post_end:
        return

    root = post_ord[post_end]

    left = indexes[root] - in_start
    right = in_end - indexes[root]

    print(root, end=" ")
    solve(in_start, in_start + left - 1, post_start, post_start + left - 1)
    solve(in_end - right + 1, in_end, post_end - right, post_end - 1)


solve(0, n - 1, 0, n - 1)
