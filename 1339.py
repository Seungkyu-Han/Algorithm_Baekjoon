import sys

N = int(sys.stdin.readline())

words = [[] for i in range(8)]

for i in range(N):
    tmp = list(sys.stdin.readline().strip())
    for t in range(len(tmp)):
        words[t].append(tmp[len(tmp) - t - 1])

alpha = [0] * 26

for i in range(8):
    if not words[i]:
        break

    for al in words[i]:
        alpha[ord(al) - 65] += 10 ** i

alpha.sort(reverse=True)

result = 0

for i in range(10):
    result += alpha[i] * (9 - i)

print(result)
