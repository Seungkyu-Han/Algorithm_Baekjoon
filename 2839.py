N = int(input())

for i in range(int(N/5)+1,0,-1):
    if (N-5*i)%3==0 and N-5*i>=0:
        print(int(i+(N-5*i)/3))
        exit()
if(N%3==0):
    print(int(N/3))
    exit()
else:
    print(-1)
