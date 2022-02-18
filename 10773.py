num = int(input())

list1 = []

for i in range(num):
    plus = int(input())
    if plus == 0:
        list1.pop()
    else:
        list1.append(plus)

print(sum(list1))
