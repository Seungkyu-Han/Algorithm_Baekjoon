N = input()

list1 = list(map(int, N))
list1.sort(reverse=True)
list1 = list(map(str, list1))
str1 = ''.join(list1)
print(str1)
