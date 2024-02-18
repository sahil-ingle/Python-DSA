def selection_sort(arr):

    for i in range(len(arr)):
        min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[min]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

    return arr

x = [2,42,4,6,3,7,2,7,1,7,234,562,3]

print(selection_sort(x))