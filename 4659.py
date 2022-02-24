def find_1(str_x):
    list1 = ['a', 'e', 'i', 'o', 'u']
    cnt = 0
    for i in list1:
        if i in str_x:
            cnt += 1
    if cnt == 0:
        return True
    else:
        return False


def find_2(str_x):
    list1 = ['a', 'e', 'i', 'o', 'u']
    lista = list(str_x)
    for i in range(len(lista)):
        if lista[i] in list1:
            lista[i] = 1
        else:
            lista[i] = 0
    if len(lista) >= 3:
        for t in range(len(lista)-2):
            if sum(lista[t:t+3]) == 0 or sum(lista[t:t+3]) == 3:
                return True

    return False


def find_3(str_x):
    list1 = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'\
             'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in list1:
        if i+i in str_x:
            return True
    return False


str1 = input()

while str1 != 'end':
    if find_1(str1):
        print('<'+str1+'> is not acceptable.')
        str1 = input()
        continue
    if find_2(str1):
        print('<' + str1 + '> is not acceptable.')
        str1 = input()
        continue
    if find_3(str1):
        print('<' + str1 + '> is not acceptable.')
        str1 = input()
        continue

    print('<' + str1 + '> is acceptable.')
    str1 = input()
