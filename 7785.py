import sys

company = dict()

N = int(sys.stdin.readline())

for i in range(N):
    name, stat = sys.stdin.readline().split()
    if stat == "enter":
        company[name] = True
    else:
        del company[name]

for name in sorted(company.keys(), reverse=True):
    print(name)
