num = int(input())

list1 = []
count = 2
while num != 1:
    if num % count == 0:
        num /= count
        list1.append(count)
    else:
        count += 1

for i in list1:
    print("%d" %i)
