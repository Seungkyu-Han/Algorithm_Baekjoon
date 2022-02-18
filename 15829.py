n = int(input())
str1 = input()

list1 = [ord(str1[i])-96 for i in range(len(str1))]

total = 0

for t in range(n):
    total += list1[t] * (31 ** t)

print(total % 1234567891)
