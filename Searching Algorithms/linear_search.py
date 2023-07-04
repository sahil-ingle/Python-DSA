def linear_search(arr, item):

    for i in range(len(arr)- 1):
        if arr[i] == item:
            return print(f"The item {item} is present at index {i}")

    print("item not found in the array")

x = [1,2,3,4,5,6]

linear_search(x, 3)