str1 = list(input())
str1.reverse()

str1 = ''.join(str1)
list1 = list(map(int, str1.split()))

print(max(list1))
