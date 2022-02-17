list1 = []

for i in range(3):
    list1.append(list(map(int, input().split())))

result = [[i[3]-i[0], i[4]-i[1], i[5]-i[2]] for i in list1]

for t in result:
    for k in [2, 1]:
        if t[k] < 0:
            t[k-1] -= 1
            t[k] += 60

for q in result:
    print(q[0], q[1], q[2])
