def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1]
    bigger_value = []
    smaller_value = []

    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            smaller_value.append(arr[i])
        else:
            bigger_value.append(arr[i])

    return quick_sort(smaller_value) + [pivot] + quick_sort(bigger_value)


x = [324, 234, 234, 2, 3, 42, 43, 23, 4, 234, 3]

print(quick_sort(x))
