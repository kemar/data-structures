def quicksort(arr, lo=0, hi=None):

    if hi is None:
        hi = len(arr) - 1  # Don't forget that lists are 0-based.

    # `lo < hi` means there is at least 2 elements.
    if lo < hi:

        # `p` is the position of the pivot in the array after partitioning.
        p = partition(arr, lo, hi)

        # Recursively sort the part that is "less than" pivot.
        quicksort(arr, lo, p - 1)

        # Recursively sort the part that is "greater than" pivot.
        quicksort(arr, p + 1, hi)

    return arr

def partition(arr, lo, hi):

    # Lomuto algorithm: pick the last item as the pivot.
    pivot_index = hi

    # We want to find the position of the pivot in the array.
    # `l` keeps track of this position. Start at `lo`.
    l = lo

    # Iterate through the array from `lo` to `hi - 1` (`hi - 1` because the pivot is at `hi`).
    for i in range(lo, hi):
        if arr[i] <= arr[pivot_index]:
            # Put elements smaller than the pivot on the left.
            swap(arr, i, l)
            l = l + 1

    # Move the pivot at its correct position.
    swap(arr, l, pivot_index)

    return l

def swap(arr, left, right):
    tmp_left = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp_left

# a = [-1, 10, 8, 20, 3]
# a = [-2, -100, 2, 1, 20, 54, 54876, -560]
a = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2]

print('-' * 40)
print(a)

b = quicksort(a)

print(b)
