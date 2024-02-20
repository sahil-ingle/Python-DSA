def fibo(num):
    if num <= 1:
        return 0
    elif num == 2:
        return 1

    a,b = 0,1
    print(a)
    print(b)

    for _ in range(num - 2):
        temp = a+b
        a = b
        b = temp
        print(temp)



n = int(input("Enter a number = "))
fibo(n)