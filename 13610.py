a, b = map(int, input().split())

count = 1
while True:
    if b * count - a * count >= b:
        break
    count += 1
print(count)
