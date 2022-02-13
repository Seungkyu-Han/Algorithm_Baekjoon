num = int(input())

count = 1
rg = 1

if num == 1:
    print(1)
    exit()

while not(rg < num <= rg + 6 * count):
    rg += 6 * count
    count += 1

print(count+1)
