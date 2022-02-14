list1 = []
list2 = []

for i in range(3):
    list1.append(int(input()))

for t in range(2):
    list2.append(int(input()))

print(min(list1) + min(list2)-50)
