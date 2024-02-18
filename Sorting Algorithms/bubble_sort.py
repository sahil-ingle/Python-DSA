def bubble_sort(arr):
    if len(arr) <= 1:
        return arr

    for i in range(len(arr) - 1):
        swap = False
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        if not swap:
            return arr




x = [2,3 ,2,334,23,423,34,234,34 ,138]

print(bubble_sort(x))