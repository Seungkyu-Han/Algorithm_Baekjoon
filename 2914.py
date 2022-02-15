list1 = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

count = 0

str1 = input()

for i in list1:
    count += str1.count(i)
    str1 = str1.replace(i, ' ' * len(i))

str1 = str1.replace(' ', '')
count += len(str1)

print(count)
