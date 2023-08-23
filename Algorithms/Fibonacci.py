def fibo(num):
    if num <= 1:
        return 0
    elif num == 2:
        return 1

    a,b = 0,1

    for _ in range(num - 2):
        temp = a+b
        a = b
        b = temp

    return temp

print(fibo(0))