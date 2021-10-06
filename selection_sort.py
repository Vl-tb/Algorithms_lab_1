'''
This module contains implementation of
selection sort algorithm.
'''
from random import randint

def selection_sort(arr: list) -> None:
    '''
    Selection sort.
    '''
    comparisons = 0

    if len(arr) < 2:
        return

    for i in range(len(arr)):
        minimum = arr[i]
        min_ind = i
        for j in range(i+1,len(arr)):
            if arr[j] <= minimum:
                minimum = arr[j]
                min_ind = j
            comparisons += 1
        arr[i], arr[min_ind] = arr[min_ind], arr[i]
    return comparisons

if __name__ == "__main__":
    arr = [randint(-10, 10) for _ in range(10)]
    print(arr)
    comparisons = selection_sort(arr)
    print(arr)
    print(comparisons)
