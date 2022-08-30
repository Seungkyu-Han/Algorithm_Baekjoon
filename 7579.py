import sys

N, M = map(int, sys.stdin.readline().split())

m_list = list(map(int, sys.stdin.readline().split()))

c_list = list(map(int, sys.stdin.readline().split()))

result = [1e9] * (M + 1)
result[0] = 0

for i in range(N):
    for t in range(M, -1, -1):
        if result[t] == 1e9:
            continue

        if t + m_list[i] > M:
            result[M] = min(result[M], result[t] + c_list[i])
        else:
            result[t + m_list[i]] = min(result[t + m_list[i]], result[t] + c_list[i])


print(result[-1])
