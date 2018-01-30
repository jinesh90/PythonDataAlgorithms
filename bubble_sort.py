"""
Example of bubble sort, in this example, Complexity is O(N*(N+1))= O(N^2+N)~=O(N^2)

"""

def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array)-1):
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
    return array



print(bubbleSort([1,3,2,6,1,3,8,9,2,4,9]))
