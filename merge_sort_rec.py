'''
This module contains implementation of
recursive merge sort algorithm.
'''
from random import randint
from math import floor, inf

def merge_sort_rec(arr: list, p: int, r: int, comparisons: int) -> None:
    '''
    Main function
    '''
    if p<r:
        mid = floor((p+r)/2)
        left = merge_sort_rec(arr, p, mid, comparisons)
        right = merge_sort_rec(arr, mid+1, r, comparisons)
        comparisons += left + right 
        comparisons += merge(arr, p, mid, r)
    return comparisons

def merge(arr: list, p: int, mid: int, r: int) -> None:
    '''
    Merge of two sorted halves.
    '''
    len_1 = mid - p + 1
    len_2 = r - mid
    comparisons = 0
    L = [0] * (len_1+1)
    R = [0] * (len_2+1)
    for i in range(len_1+1):
        L[i] = arr[p+i]
    for i in range(len_2):
        R[i] = arr[mid+i+1]
    L[-1] = inf
    R[-1] = inf
    i = 0
    j = 0
    for k in range(p, r+1):
        comparisons += 1
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
    return comparisons

if __name__ == "__main__":
    arr = [randint(-10, 10) for _ in range(10)]
    print(arr)
    comparisons = merge_sort_rec(arr, 0, len(arr)-1, 0)
    print(arr)
    print(comparisons)
