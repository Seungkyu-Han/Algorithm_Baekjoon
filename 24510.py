num = int(input())

max_cnt = 0

for i in range(num):
    cnt = 0
    str1 = input()
    cnt += str1.count('for')
    cnt += str1.count('while')
    if cnt > max_cnt:
        max_cnt = cnt

print(max_cnt)
