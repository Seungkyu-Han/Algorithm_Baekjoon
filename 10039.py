list1 = []

for i in range(5):
    score = int(input())
    if score >= 40:
        list1.append(score)
    else:
        list1.append(40)

print(sum(list1)//5)
