import sys

num = int(sys.stdin.readline())

max_result = [0, 0, 0]
min_result = [0, 0, 0]


for i in range(num):
    game = list(map(int, sys.stdin.readline().split()))
    max_temp1 = max(max_result[0:2]) + game[0]
    max_temp2 = max(max_result) + game[1]
    max_temp3 = max(max_result[1:3]) + game[2]
    max_result = [max_temp1, max_temp2, max_temp3]
    min_temp1 = min(min_result[0:2]) + game[0]
    min_temp2 = min(min_result) + game[1]
    min_temp3 = min(min_result[1:3]) + game[2]
    min_result = [min_temp1, min_temp2, min_temp3]

print(max(max_result), min(min_result))
