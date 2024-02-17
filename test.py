num = [2, 234, 234, 234, 234, 234, 423, 23, 235, 2535, 4, 5462, 6123, 63, 461, 345, 134, 635, 6, 256, 34]

def merge_sort(arr):
    if len(arr) <=1:
        return arr

    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j +1] = arr[j+1] , arr[j]

    return arr


print(merge_sort(num))


def binary_serach(x, arr):
    left = 0
    right = len(arr) - 1
    mid = (left + right)//2

    for i in range(len(arr) - 1):
        mid = (left + right)//2
        if arr[mid] == x:
            return "found it at index " + str(mid)
        if arr[mid] < x:
            left = mid
        else:
            right = mid

    return "its not in the list"

print(binary_serach(234,num))

n = "00000010100101000001111010011100"
bit_num = int(n, 2)
print(bit_num)

bit_val = bin(bit_num)
bit_val = str(bit_val)[2:]
bit_val = bit_val[::-1]
bit_num = int(bit_val, 2)
print(bit_num)


