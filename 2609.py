a, b = map(int, input().split())

mimi = 1
mama = max(a, b)

for i in range(min(a, b), 0, -1):
    if a % i == 0 and b % i == 0:
        mimi = i
        break

while not(mama % a == 0 and mama % b == 0):
    mama += max(a, b)

print(mimi)
print(mama)
