import sys

index = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

target = sys.stdin.readline().strip()

result = index.index(target) * 10

target = sys.stdin.readline().strip()

result += index.index(target)

target = sys.stdin.readline().strip()

result *= 10 ** index.index(target)

print(result)
