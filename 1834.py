num = int(input())

cnt = 1
total = 0

while cnt < num:
    total += (num * cnt) + cnt
    cnt += 1

print(total)
