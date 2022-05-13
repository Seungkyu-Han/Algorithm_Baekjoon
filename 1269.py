import sys

N, M = map(int, sys.stdin.readline().split())

lista = set(map(int, sys.stdin.readline().split()))
listb = set(map(int, sys.stdin.readline().split()))

print(len(lista - listb) + len(listb - lista))
