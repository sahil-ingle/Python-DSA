def countSubArrayProductLessThanK(a, n, k):
    if n == 0:
        return 0

    no_subarr = 0
    start = 0
    product = 1

    for end in range(n):
        product *= a[end]

        while product >= k and start <= end:
            product /= a[start]
            start += 1

        no_subarr += end - start + 1

    return no_subarr

a = [1, 2, 3, 4]
print(countSubArrayProductLessThanK(a, 4, 10))
#expected answer is 7
