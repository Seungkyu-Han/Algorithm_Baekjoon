num = int(input())

for i in range(num):
    list1 = input()
    list1 = list1.replace(" ","")
    for x in list1[1:]:
        print(x*int(list1[0]), end = '')
    print()
