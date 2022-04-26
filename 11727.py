num = int(input())

prev = 1
cur = 3

if num == 1:
    cur = 1
elif num == 2:
    cur = 3
else:
    for i in range(num-2):
        tmp = cur + 2 * prev
        prev = cur
        cur = tmp

print(cur % 10007)
