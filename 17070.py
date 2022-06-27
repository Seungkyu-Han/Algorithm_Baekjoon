from collections import deque
import sys

num = int(sys.stdin.readline())

house = []
result = 0

for i in range(num):
    house.append(list(map(int, sys.stdin.readline().split())))

need_visit = deque()
need_visit.append([0, 1, 1])

while need_visit:
    x, y, pipe_type = need_visit.pop()
    if x == num - 1 and y == num - 1:
        result += 1
        continue
    bool_x = True if 0 <= x + 1 < num else False
    bool_y = True if 0 <= y + 1 < num else False

    if pipe_type == 1:
        if bool_y and house[x][y + 1] == 0:
            need_visit.append([x, y + 1, 1])
            if bool_x:
                if house[x+1][y] + house[x+1][y+1] == 0:
                    need_visit.append([x + 1, y + 1, 2])
    elif pipe_type == 2:
        if bool_y and house[x][y + 1] == 0:
            need_visit.append([x, y + 1, 1])
            if bool_x:
                if house[x + 1][y] + house[x + 1][y + 1] == 0:
                    need_visit.append([x + 1, y + 1, 2])
        if bool_x and house[x + 1][y] == 0:
            need_visit.append([x + 1, y, 3])
    else:
        if bool_x and house[x + 1][y] == 0:
            if bool_y:
                if house[x][y + 1] + house[x + 1][y + 1] == 0:
                    need_visit.append([x + 1, y + 1, 2])
            need_visit.append([x + 1, y, 3])
print(result)
