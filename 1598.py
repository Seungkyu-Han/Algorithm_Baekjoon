def lim(n):
    if n // 4 == n / 4:
        return n // 4
    else:
        return (n // 4) + 1


def na_nu(n):
    if n % 4 == 0:
        return 4
    else:
        return n % 4


n1, n2 = map(int, input().split())

list1 = [lim(n1), na_nu(n1)]
list2 = [lim(n2), na_nu(n2)]

print(abs(list1[0]-list2[0])+abs(list1[1]-list2[1]))
