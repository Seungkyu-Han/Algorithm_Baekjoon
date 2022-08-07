import sys

D, P = map(int, sys.stdin.readline().split())

visited = dict()
result = -1


def solve(value, cnt):
    global result
    if cnt == P:
        result = max(result, value)
        return

    for i in range(2, 10):
        if len(str(value * i)) <= D:
            if value * i in visited:
                if visited[value * i] > cnt + 1:
                    visited[value * i] = cnt + 1
                    solve(value * i, cnt + 1)
            else:
                visited[value * i] = cnt + 1
                solve(value * i, cnt + 1)


solve(1, 0)
print(result)
