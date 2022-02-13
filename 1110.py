num = int(input())

cnt = 1
    
new_num = num%10*10 + (num//10+num%10)%10

while(True):
    if new_num == num:
        print(cnt)
        break
    new_num = new_num%10*10 + (new_num//10+new_num%10)%10
    cnt +=1
