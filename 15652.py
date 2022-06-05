N, M = map(int, input().split())

result = []

def myresult(start):
    if len(result) == M:
        print(*result)
        return

    for i in range(start, N + 1):
        result.append(i)
        myresult(i)
        result.pop()
myresult(1)
