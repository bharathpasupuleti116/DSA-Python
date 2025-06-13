def find_largest(arr):
    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

def find_smallest(arr):
    min_num = arr[0]

    for num in arr:
        if num < min_num:
            min_num = num
    return min_num

arr = [23,34,5.6,65,89]
print('largest element:', find_largest(arr))
print('smallest element:', find_smallest(arr))