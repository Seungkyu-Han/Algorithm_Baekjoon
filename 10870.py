def fibo(a):
    if a == 0:
        result = 0
    elif a == 1:
        result = 1
    else:
        result = fibo(a-1) + fibo(a-2)

    return result

num = int(input())

print(fibo(num))

