N, M = map(int, input().split())

list1 = [i + 1 for i in range(N)]

cnt = 1

result = []

while len(list1) > 0:
    if cnt == M:
        result.append(list1.pop(0))
        cnt = 1
    else:
        list1.append(list1.pop(0))
        cnt += 1

print('<', end='')

for i in range(len(result)):
    if i == len(result) - 1:
        print(result[i], end='')
    else:
        print(result[i], end=', ')

print('>', end='')
