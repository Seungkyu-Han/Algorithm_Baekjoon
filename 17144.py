import sys, copy

R, C, T = map(int, sys.stdin.readline().split())

dust = []
cleaner = ()

for i in range(R):
    dust.append(list(map(int, sys.stdin.readline().split())))

for i in range(R):
    if dust[i][0] == -1:
        cleaner = (i, i + 1)
        break


def spread(dust_list):
    result = [[0] * C for _ in range(R)]
    for t in range(R):
        for k in range(C):
            if dust_list[t][k] > 0:
                cnt = 0
                for x_ptr, y_ptr in ((t - 1, k), (t + 1, k), (t, k - 1), (t, k + 1)):
                    if 0 <= x_ptr < R and 0 <= y_ptr < C:
                        if y_ptr == 0 and (x_ptr in cleaner):
                            continue
                        result[x_ptr][y_ptr] += dust_list[t][k] // 5
                        cnt += 1
                result[t][k] += (dust[t][k] - ((dust[t][k] // 5) * cnt))
    return result


def clean_up(dust_list):
    result = copy.deepcopy(dust_list)
    # up
    result[cleaner[0]] = [0] + dust_list[cleaner[0]][:-1]
    for t in range(cleaner[0]):
        result[t][-1] = dust_list[t + 1][-1]
    result[0][:-1] = dust_list[0][1:]
    for t in range(cleaner[0]):
        result[t+1][0] = dust_list[t][0]
    # down
    result[cleaner[1]] = [0] + dust_list[cleaner[1]][:-1]
    for t in range(R - cleaner[1] - 1):
        result[cleaner[1] + t + 1][-1] = dust_list[cleaner[1] + t][-1]
    result[-1][:-1] = dust_list[-1][1:]
    for t in range(R - cleaner[1] - 1):
        result[R - 2 - t][0] = dust_list[R - 1 - t][0]

    result[cleaner[0]][0], result[cleaner[1]][0] = -1, -1
    return result


for i in range(T):
    dust = spread(dust)
    dust = clean_up(dust)

dust[cleaner[0]][0], dust[cleaner[1]][0] = 0, 0
result = 0

for q in range(R):
    for w in range(C):
        result += dust[q][w]

print(result)
