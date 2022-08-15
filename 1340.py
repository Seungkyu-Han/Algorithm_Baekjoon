import sys

cur = list(sys.stdin.readline().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
change = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

cur[0] = change.index(cur[0])

if int(cur[2]) % 400 == 0 or (int(cur[2]) % 4 == 0 and int(cur[2]) % 100 != 0):
    month[1] = 29

day = (int(cur[3][0:2]) * 60 + int(cur[3][3:5])) / 1440

for i in range(cur[0]):
    day += month[i]

day += (int(cur[1][:-1]) - 1)
print(day / sum(month) * 100)
