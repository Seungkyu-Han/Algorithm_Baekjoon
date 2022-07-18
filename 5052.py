import sys


class PhoneNumberBook:
    class Numbers:
        def __init__(self, my_bool):
            self.bool = my_bool
            self.next = [None for i in range(10)]

    def __init__(self):
        self.head = self.Numbers(False)

    def to_plus_number(self, plus_number, cur=None):

        if cur is None:
            cur = self.head

        if cur.bool:
            return False

        if len(plus_number) == 0:
            cur.bool = True
            return True

        target = plus_number[0]
        if cur.next[target] is None:
            cur.next[target] = self.Numbers(False)

        return self.to_plus_number(plus_number[1:], cur.next[target])


t = int(sys.stdin.readline())

for i in range(t):
    mytree = PhoneNumberBook()
    cnt = int(sys.stdin.readline())
    flag = True
    plus = []
    for t in range(cnt):
        plus.append(list(map(int, sys.stdin.readline().strip())))
    plus.sort(key=lambda x: len(x))
    for t in range(cnt):
        go = mytree.to_plus_number(plus[t])
        if go is False:
            flag = False
            break
    if flag:
        print("YES")
    else:
        print("NO")
