m, d = map(int, input().split())

list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = d

for i in range(m - 1):
    total += list1[i]

days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

print(days[total % 7])
