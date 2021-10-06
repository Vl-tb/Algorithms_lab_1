'''
This module contains implementation of
shell sort algorithm.
'''
from random import randint
from math import floor

def shell_sort(arr: list) -> None:
    '''
    Shell sort
    '''
    comparisons = 0

    if len(arr) < 2:
        return

    k = floor(len(arr)/2)
    i = 0
    j = -1
    while k > 0:
        param = 0
        if arr[i] >= arr[i+k]:
            arr[i], arr[i+k] = arr[i+k], arr[i]
            if i-k > -1:
                param = 1
                if j == -1:
                    j = i
                i = i - k - 1
        if j != -1 and not param:
            i = j
            j = -1
        comparisons += 1
        i += 1
        if i+k == len(arr):
            i = 0
            k = floor(k/2)
    return comparisons

if __name__ == "__main__":
    arr = [randint(-10, 10) for _ in range(10)]
    print(arr)
    comparisons = shell_sort(arr)
    print(arr)
    print(comparisons)
