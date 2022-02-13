def fac (a):
    result = 1
    if a > 0 :
        result = fac(a-1) * a
    return result

num = int(input())

print(fac(num))
