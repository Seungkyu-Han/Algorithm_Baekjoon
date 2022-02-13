num = int(input())
def han( num ):
    if num < 100:
        count = num
    else:
        count = 99
        nu = [1, 0, 0]
        for i in range(100, num+1):
            nu = map(int, str(i))
            if nu[2] - nu[1] == nu[1] - nu[0]:
                count += 1

    return count

print(han(num))

