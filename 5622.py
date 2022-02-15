list1 = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

S = input()
cnt = 0
for i in range(len(S)):
    for x in range(len(list1)):
        if S[i] in list1[x]:
            cnt += (3 + x)
            break

print(cnt)
