list1 = map(int, input().split())
total = 0
for i in list1:
    total += i**2

print(total%10)
