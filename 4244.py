num = int(input())

for i in range(num):
    list1 = list(map(int, input().split(" ")))
    average = sum(list1[1:])/list1[0]
    good = 0.0
    for x in list1[1:]:
        if(x > average):
            good+=1
    print(f'{good/list1[0]*100:.3f}%')
