def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = arr[:mid]
    right_arr = arr[mid:]

    merge_sort(left_arr)
    merge_sort(right_arr)

    i, j, k = 0, 0, 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1

    return arr


x = [2, 2, 44, 324, 54345, 324, 54, 324, 43, 61, 46, 1, 23]

print(merge_sort(x))
