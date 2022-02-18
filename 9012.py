num = int(input())

for _ in range(num):
    str1 = input()
    while '()' in str1:
        str1 = str1.replace('()', '')
    if len(str1) == 0:
        print('YES')
    else:
        print('NO')
