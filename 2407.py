import sys

n, m = map(int, sys.stdin.readline().split())

n_result = 1
m_result = 1

for i in range(m):
    n_result *= n
    n -= 1

for i in range(1, m + 1):
    m_result *= i

print(n_result//m_result)
