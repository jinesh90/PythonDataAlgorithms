"""
Example of selection sort, in this example, Complexity is O(N*N+1)) = O(N^2+1) ~= O(N^2)

"""

def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        smallIndex = i
        for j in range(i+1, n):
            if array[j] < array[smallIndex]:
                smallIndex = j
        if i != smallIndex:
            array[i],array[smallIndex] = array[smallIndex],array[i]

    return array


print(selectionSort([1,3,2,6,1,3,8,9,2,4,9]))


