from collections import Counter
import sys


def average(listx):
    total = sum(listx)

    result = sum(listx)//len(listx) if sum(listx)/len(listx) - sum(listx)//len(listx) < 0.5 else sum(listx)//len(listx) + 1
    return result


def middle(listx):
    return listx[int((len(list1) - 1) / 2)]


def maxcnt(listx):
    counter = Counter(listx).most_common(2)
    if len(counter) > 1:
        if counter[0][1] == counter[1][1]:
            print(counter[1][0])
        else:
            print(counter[0][0])
    else:
        print(counter[0][0])


def myrange(listx):
    return max(listx) - min(listx)


num = int(sys.stdin.readline())

list1 = [int(sys.stdin.readline()) for i in range(num)]

list1.sort()

print(average(list1))
print(middle(list1))
maxcnt(list1)
print(myrange(list1))
