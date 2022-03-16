num = int(input())

list1 = ['' for i in range(num)]

for i in range(num):
    str1 = input()
    my_str = 'a'
    for t in range(1, len(str1)):
        if str1[t] in str1[:t]:
            my_str += my_str[str1.index(str1[t])]
        else:
            my_str += chr(ord(max(my_str)) + 1)
    list1[i] = my_str

cnt = 0

for i in range(len(list1)-1):
    cnt += list1[i+1:].count(list1[i])

print(cnt)
