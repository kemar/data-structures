"""
Bubble Sort
https://www.pythoncentral.io/bubble-sort-implementation-guide/

A bubble sort takes an unsorted list and keeps comparing each element with its right side neighbour in order to sort the data. Whichever element is smaller gets shifted to the left. After completion of one round, the largest number ends up in its correct position. In other words, the largest number bubbles to the top. Then, the process is repeated again and again until all of the data is sorted.

1. For the first iteration, compare all the elements (n). For the subsequent runs, compare (n-1) (n-2) and so on
2. Compare each element with its right side neighbour
3. Swap the smallest element to the left
4. Keep repeating steps 1-3 until the whole list is covered

This algorithm is of O(n^2).
"""

def bubblesort(arr):

    # Setting the range for comparison (first round: n, second round: n-1  and so on).
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]

    return arr

def bubblesort2(arr):

    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

a = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2]

b = bubblesort(a)

print(b)

c = [1,-2,-2,5,8,1254,654,-2,-2,-2,-2,-2,-2,-2,-2,-2,-2,7,5,-589.4,1,4,9,20,-2,-2,-2,-2,-2,-2]

d = bubblesort(c)

print(d)
