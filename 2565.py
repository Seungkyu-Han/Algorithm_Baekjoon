import sys

cnt = int(sys.stdin.readline())

line = [[0, 0]] * cnt

for i in range(cnt):
    line[i] = list(map(int, sys.stdin.readline().split()))

line.sort()

result = []

for i in range(cnt):
    tmp_max = 1
    tmp_result = [[1, [i]]]
    for tmp_cnt, tmp_list in result:
        flag = True
        for t in tmp_list:
            if (line[i][0] - line[t][0]) * (line[i][1] - line[t][1]) <= 0:
                flag = False
                break
        if flag:
            if tmp_max == tmp_cnt + 1:
                tmp_result.append([tmp_cnt + 1, tmp_list + [i]])
            elif tmp_max < tmp_cnt + 1:
                tmp_max = tmp_cnt + 1
                tmp_result = [[tmp_cnt + 1, tmp_list + [i]]]
    result.extend(tmp_result)

result.sort()
print(cnt - result[-1][0])
