"""
count sort, non comparision sorting if elements are limited to M
"""


def count_sort(array, num_range):
    m = [0]*(num_range + 1)
    sorted_array = []
    for i in array:
        m[i] += 1
    for i in range(1, len(m)):
        sorted_array += [i]*m[i]
    return sorted_array


print(count_sort([1,1,2,1,3,1,4,5,2,4,2,2,1,3,3,3,1,1,4,2,2,3,5,4,1], 5))

