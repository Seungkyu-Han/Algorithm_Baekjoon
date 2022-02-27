while True:
    str1 = list(input())
    list1 = []
    if str1 == ['.']:
        break
    for i in range(len(str1)):
        if str1[i] == '[' or str1[i] == ']' or str1[i] == '(' or str1[i] == ')':
            list1.append(str1[i])
    list1 = ''.join(list1)
    while '()' in list1 or '[]' in list1:
        list1 = list1.replace('()', '')
        list1 = list1.replace('[]', '')
    if len(list1) == 0:
        print('yes')
    else:
        print('no')
