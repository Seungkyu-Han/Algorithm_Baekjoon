import sys

N, M = map(int, sys.stdin.readline().split())

house = []
chicken = []
ret = 100000000

for i in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for t in range(N):
        if tmp[t] == 1:
            house.append((i, t))
        elif tmp[t] == 2:
            chicken.append((i, t))


def backtracking(cur_list, cur_index, cur_cnt):
    if cur_cnt == M:
        dist(cur_list)

    for k in range(cur_index + 1, len(chicken)):
        backtracking(cur_list + [chicken[k]], k, cur_cnt + 1)


def dist(cur_list):
    global ret

    result = 0

    for k in house:
        fun_tmp = 2500
        for q in cur_list:
            fun_tmp = min(fun_tmp, abs(k[0] - q[0]) + abs(k[1] - q[1]))
        result += fun_tmp

    ret = min(ret, result)


backtracking([], -1, 0)

print(ret)
