num = int(input())

prev = 1
cur = 2

if num == 1:
    cur = 1
elif num == 2:
    cur = 2
else:
    for i in range(num-2):
        tmp = cur + prev
        prev = cur
        cur = tmp

print(cur % 10007)
