num = int(input())

tree = {chr(i+65): [] for i in range(num)}

for i in range(num):
    parent, left, right = map(str, input().split())
    tree[parent] = [left, right]

pre = []
mid = []
fi = []


def case1(target):
    pre.append(target)
    if tree[target][0] != '.':
        case1(tree[target][0])
    if tree[target][1] != '.':
        case1(tree[target][1])
    return


def case2(target):
    if tree[target][0] != '.':
        case2(tree[target][0])
    mid.append(target)
    if tree[target][1] != '.':
        case2(tree[target][1])


def case3(target):
    if tree[target][0] != '.':
        case3(tree[target][0])
    if tree[target][1] != '.':
        case3(tree[target][1])
    fi.append(target)


case1('A')
case2('A')
case3('A')

print(''.join(pre))
print(''.join(mid))
print(''.join(fi))
