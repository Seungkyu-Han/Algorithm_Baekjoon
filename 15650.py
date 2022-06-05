N, M = map(int, input().split())

result = []

def myresult(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N + 1):
        if i not in result:
            result.append(i)
            myresult(i + 1)
            result.pop()
myresult(1)
