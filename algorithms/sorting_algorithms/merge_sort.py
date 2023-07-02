def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2

    left_arr = []
    right_arr = []

    for i in range(len(arr) - 1):
        if arr[i] <= arr[mid]:
            left_arr.append(arr[i])
        else:
            right_arr.append(arr[i])

    if len(left_arr) == 1 and len(right_arr) == 0:
        return merge_sort(left_arr)
    if len(right_arr) == 1 and len(left_arr) == 0:
        return merge_sort(right_arr)

    if len(left_arr) == 1 and len(right_arr) == 1:
        if left_arr[0] > right_arr[0]:
            return right_arr + left_arr
        else:
            return left_arr + right_arr

    return merge_sort(left_arr) + merge_sort(right_arr)


x = [2, 2, 44, 324, 54345, 324, 54, 324, 43, 61, 46, 1, 23]

print(merge_sort(x))
