ti = int(input())

if ti % 10 != 0:
    print(-1)
else:
    print("{} {} {}" .format(ti//300, ti % 300//60, ti % 60//10))
