n, m = map(int, input().split())

list1 = []
count = []

for i in range(n):
    list1.append(input())

for i in range(n-7):
    for t in range(m-7):
        cnt1 = 0
        cnt2 = 0
        for q in range(i, i+8):
            for w in range(t, t+8):
                if (q + w) % 2 == 0:
                    if list1[q][w] != 'W':
                        cnt1 += 1
                    if list1[q][w] != 'B':
                        cnt2 += 1
                else:
                    if list1[q][w] != 'B':
                        cnt1 += 1
                    if list1[q][w] != 'W':
                        cnt2 += 1

        count.append(min(cnt1, cnt2))

print(min(count))
