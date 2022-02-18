list1 = [0, 1]

num = int(input())

for i in range(1, num):
    list1.append(list1[i]+list1[i-1])

print(list1[num])
