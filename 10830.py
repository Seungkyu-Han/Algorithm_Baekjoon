import sys

A, B = map(int, sys.stdin.readline().split())


def multi(matrix1, matrix2):
    answer = [[0] * A for i in range(A)]
    for i in range(A):
        for j in range(A):
            for k in range(A):
                answer[i][j] += matrix1[i][k] * matrix2[k][j]
            answer[i][j] %= 1000
    return answer


def result(matrix, power):
    if power > 1:
        if power % 2 == 1:
            tmp = result(matrix, power//2)
            return multi(multi(tmp, tmp), matrix)
        else:
            tmp = result(matrix, power//2)
            return multi(tmp, tmp)
    else:
        answer = [[0] * A for i in range(A)]
        for i in range(A):
            for t in range(A):
                answer[i][t] += (matrix[i][t] % 1000)
        return answer


mymatrix = [0] * A

for i in range(A):
    mymatrix[i] = list(map(int, sys.stdin.readline().split()))

result_matrix = result(mymatrix, B)

for i in result_matrix:
    print(*i)
