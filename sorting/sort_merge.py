"""
Merge Sort can be used to sort an unsorted list or to merge two sorted lists.

1. Split the unsorted list into halves recursively until it can no more be divided
2. Compare each of the elements and then group them
3. Repeat step 2 until the whole list is merged and sorted in the process
"""

def mergesort(arr):

    if len(arr) == 1:
        return arr

    middle = len(arr) // 2  # Ensure int.

    # Split array in both parts.
    a = mergesort(arr[:middle])
    b = mergesort(arr[middle:])

    return merge(arr, a, b)

def merge(arr, a, b):

    # Indexes to keep track of the progress in the 3 arrays.
    # Don't forget that `arr` is just the combination of `a` + `b`.
    i = 0
    j = 0
    k = 0

    # While `a` and `b` have elements.
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

    # At this point, either `a` or `b` is empty.
    # We no longer need to do comparisons. Just append the rest of the contents.
    while i < len(a):
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        arr[k] = b[j]
        j += 1
        k += 1

    return arr

a = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2]
b = mergesort(a)
print(b)
