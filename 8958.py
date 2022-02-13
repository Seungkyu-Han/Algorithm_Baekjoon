num = int(input())

total = 0
score = 0
for i in range(num):
    list1 = list(input())
    for i in range(len(list1)):
        if list1[i] == 'O':
            score += 1
            total += score
        else:
            score = 0
    
    print(total)
    score = 0
    total = 0
