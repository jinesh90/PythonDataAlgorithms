"""
Binary search recursive way
"""

def binarySearch(array, target):
    mid = len(array)//2
    if mid >= 0 and len(array) > 1:
        if target > array[mid]:
            return binarySearch(array[mid:], target)
        elif target < array[mid]:
            return binarySearch(array[:mid], target)
        elif target == array[mid]:
            return True
    return False

print(binarySearch([1,3,5,7,9],6))

"""
Binary search normal way
"""

def binarySearchNormal(array, target):
    low = 0
    high = len(array) -1

    while low <= high:
        mid = (high + low)//2
        if array[mid] == target:
            return True
        if array[mid] < target:
            low = mid+1
        if array[mid] > target:
            high = mid -1
    return False

print(binarySearchNormal([1,3,5,7,9],7))