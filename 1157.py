s = input()
s = list(s.upper())
list1 = list(set(s))
cnt = []

for i in range(len(list1)):
  cnt.append(s.count(list1[i]))

if (cnt.count(max(cnt)) >= 2):
  print("?")
else:
  print(list1[cnt.index(max(cnt))])
