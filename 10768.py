month = int(input())

days = int(input())

if month == 2 and days == 18:
    print('Special')
elif month < 2:
    print('Before')
elif month == 2 and days < 18:
    print('Before')
else:
    print('After')
