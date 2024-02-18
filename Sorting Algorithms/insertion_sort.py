def insertion_sort(arr):
    for i in range(len(arr)):
        key = arr[i]

        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


    return arr

x = [2,42,4,6,3,7,2,7,1,7,234,562,3]
print(insertion_sort(x))