
def merge(b, c):
    d = list()
    while b!=[] and c!=[]:
        if b[0] > c[0]:
            d.append(c[0])
            c.pop(0)
        else:
            d.append(b[0])
            b.pop(0)
    else:
        if b == []:
            d += c
        else:
            d += b
    return d


def mergesort(array):
    n = len(array)
    if n == 1:
        return array
    midpoint = len(array) // 2
    b = mergesort(array[:midpoint])
    c = mergesort(array[midpoint:])
    sorted_array = merge(b, c)
    return sorted_array


print(mergesort([3,6,7,8,9,1,2,4,5]))