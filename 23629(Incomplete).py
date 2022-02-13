import sys

S = sys.stdin.readline()

list_o = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX',
          'SEVEN', 'EIGHT', 'NINE', 'x', '/']
list_t = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '*', '//']


for q in range(len(list_o)):
    S = S.replace(list_o[q], list_t[q])

list1 = ['+', '-', '*', '//']
list2 = []
for i in list1:
    for x in list1:
        list2.append('{}{}'.format(i, x))

code = 0
for t in list2:
    if t in S:
        print('Madness!')
        code += 1
        break

if code == 0:
    S = S.replace('=', '')
    S = S.rstrip()
    s = str(eval(S))
    for q in range(len(list_o)):
        s = s.replace(list_t[q], list_o[q])
    print("{}=" .format(S))
    print(s)
