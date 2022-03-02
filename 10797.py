num = int(input())

list1 = map(int, input().split())

cnt = 0

for i in list1:
    if num == i % 10:
        cnt += 1
        
print(cnt)
