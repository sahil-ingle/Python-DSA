def binary_search(arr, item):

    left_index = 0
    right_index = len(arr) - 1

    while left_index <= right_index:
        mid = (left_index + right_index) // 2

        if arr[mid] == item:
            return mid
        if item > arr[mid]:
            left_index = mid + 1
        else:
            right_index = mid - 1

    return -1


x = [1,2,3,4,5,6]

print(binary_search(x, 6))