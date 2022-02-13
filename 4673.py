re = []
for i in range(1, 10001):
    re.append(sum(map(int, str(i))))
    re[i-1] += i

for x in range(1, 10001):
    if x not in re:
        print(x)
