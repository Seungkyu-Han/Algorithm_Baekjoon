N = int(input())

tmp_prime = [True] * (N + 1)

rootN = int(N**0.5)

for i in range(2, rootN + 1):
    if tmp_prime[i]:
        for j in range(i + i, N + 1, i):
            tmp_prime[j] = False

prime = [i for i in range(2, N + 1) if tmp_prime[i] is True]

left, right = 0, 0
length = len(prime)
cur = prime[0] if prime else 0
result = 0

while right < length:
    if cur == N:
        result += 1
        right += 1
        if right >= length:
            break
        cur += prime[right]
    elif cur < N:
        right += 1
        if right >= length:
            break
        cur += prime[right]
    else:
        cur -= prime[left]
        left += 1

print(result)
