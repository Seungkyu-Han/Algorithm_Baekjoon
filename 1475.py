N = input()

list1 = list(map(int, N))
list2 = [list1.count(i) for i in range(9)]
list2[6] += list1.count(9)
list2[6] = list2[6]//2 + list2[6] % 2

print(max(list2))
