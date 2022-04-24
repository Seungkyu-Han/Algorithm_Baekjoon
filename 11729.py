def hanoi(num, fr, tmp, to):
    if num == 1:
        print(fr, to)
    else:
        hanoi(num - 1, fr, to, tmp)
        print(fr, to)
        hanoi(num - 1, tmp, fr, to)


n = int(input())

print(2 ** n - 1)

hanoi(n, 1, 2, 3)
