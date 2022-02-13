s = input()

for i in range(26):
    print("%d" % (s.find(chr(97+i))), end=" ")
