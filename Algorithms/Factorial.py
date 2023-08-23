def factorial(num):
    if num == 0:
        return 1
    fact = num
    while num > 1:
        fact = fact * (num-1)
        num -= 1
    return fact

print(factorial(2))