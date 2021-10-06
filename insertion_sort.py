'''
This module contains implementation of
insertion sort algorithm.
'''
from random import randint

def insertion_sort(arr: list) -> int:
    '''
    Insertion sort.
    '''
    comparisons = 0
    if len(arr) < 2:
        return
    i = 1
    j = 0
    while i < len(arr):
        value = arr[i]
        while value < arr[j] and j >= 0 :
            comparisons += 1
            arr[j+1] = arr[j]
            arr[j] = value
            j -= 1
        comparisons += 1
        i += 1
        j = i - 1
    comparisons += 1
    return comparisons

if __name__ == "__main__":
    arr = [randint(-10, 10) for _ in range(10)]
    print(arr)
    comparisons = insertion_sort(arr)
    print(arr)
    print(comparisons)
