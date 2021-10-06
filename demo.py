'''
This module is main for comparing 4 algorithms:
insertion sort, selection sort, merge sort and shell sort.
'''
import time
from math import log2
from random import randint
from insertion_sort import insertion_sort
from selection_sort import selection_sort
from merge_sort_rec import merge_sort_rec, merge
from shell_sort import shell_sort
import matplotlib.pyplot as plt


def main(param=1) -> None:
    '''
    Starts simulations. Writes data to .txt file.
    If param == 1:
        run simulations for new data and build graphs;
        !!! Runs approximately 25 min.
    elif param == 0:
        read .txt file and build graphs.
    ex_1 - sorts array with random numbers;
    ex_2 - sorts array, numbers in which are in increasing order;
    ex_3 - sorts array, numbers in which are in decreasing order;
    ex_4 - sorts array, which consist only of {1,2,3}.
    '''
    if param:
        exp_1 = ex_1()
        exp_2 = ex_2()
        exp_3 = ex_3()
        exp_4 = ex_4()
        with open('data.txt','w', encoding='utf-8') as file:
            file.write(str(exp_1)+'\n')
            file.write(str(exp_2)+'\n')
            file.write(str(exp_3)+'\n')
            file.write(str(exp_4)+'\n')

        graph_1, graph_2 = graph_build(exp_1, 1)
        graph_3, graph_4 = graph_build(exp_2, 3)
        graph_5, graph_6 = graph_build(exp_3, 5)
        graph_7, graph_8 = graph_build(exp_4, 7)
        plt.show()

    else:
        with open('data.txt', 'r', encoding='utf-8') as file:
            data = file.readlines()
    
        graph_1, graph_2 = graph_build(eval(data[0][:-1]), 1)
        graph_3, graph_4 = graph_build(eval(data[1][:-1]), 3)
        graph_5, graph_6 = graph_build(eval(data[2][:-1]), 5)
        graph_7, graph_8 = graph_build(eval(data[3][:-1]), 7)
        plt.show()
    


def ex_1():
    results = [[[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]]]
    methods = ['insertion_sort(', 'selection_sort(', 'merge_sort_rec(', 'shell_sort(']
    for j in range(7,16):
        for t in range(5):
            arr = [randint(-2**j, 2**j) for _ in range(2**j)]
            for index, method in enumerate(methods):
                if index == 2:
                    args = ', 0, 2**j-1, 0'
                else:
                    args = ''
                start = time.time()
                comparisons = eval(method + f'{arr}'+ args +')')
                finish = time.time() - start
                results[j-7][index][0] += comparisons
                results[j-7][index][1] += finish
        for pair in results[j-7]:
            pair = [round(pair[0]/5, 10), round(pair[1]/5, 10)]
    return results


def ex_2():
    results = [[[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]]]
    methods = ['insertion_sort(', 'selection_sort(', 'merge_sort_rec(', 'shell_sort(']
    for j in range(7,16):
        arr = [randint(-2**j, 2**j) for _ in range(2**j)]
        merge_sort_rec(arr, 0, len(arr)-1, 0)
        for index, method in enumerate(methods):
            if index == 2:
                args = ', 0, 2**j-1, 0'
            else:
                args = ''
            start = time.time()
            comparisons = eval(method + f'{arr}'+ args +')')
            finish = time.time() - start
            results[j-7][index][0] += comparisons
            results[j-7][index][1] += finish
    return results


def ex_3():
    results = [[[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]]]
    methods = ['insertion_sort(', 'selection_sort(', 'merge_sort_rec(', 'shell_sort(']
    for j in range(7,16):
        arr = [randint(-2**j, 2**j) for _ in range(2**j)]
        merge_sort_rec(arr, 0, len(arr)-1, 0)
        arr = arr[::-1]
        for index, method in enumerate(methods):
            if index == 2:
                args = ', 0, 2**j-1, 0'
            else:
                args = ''
            start = time.time()
            comparisons = eval(method + f'{arr}'+ args +')')
            finish = time.time() - start
            results[j-7][index][0] += comparisons
            results[j-7][index][1] += finish
    return results


def ex_4():
    results = [[[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]],
                [[0,0],[0,0],[0,0],[0,0]]]
    methods = ['insertion_sort(', 'selection_sort(', 'merge_sort_rec(', 'shell_sort(']
    for j in range(7,16):
        for t in range(3):
            arr = [randint(1, 3) for _ in range(2**j)]
            for index, method in enumerate(methods):
                if index == 2:
                    args = ', 0, 2**j-1, 0'
                else:
                    args = ''
                start = time.time()
                comparisons = eval(method + f'{arr}'+ args +')')
                finish = time.time() - start
                results[j-7][index][0] += comparisons
                results[j-7][index][1] += finish
        for pair in results[j-7]:
            pair = [round(pair[0]/3, 10), round(pair[1]/3, 10)]
    return results

def graph_build(data: list, n: int) -> object:
    '''
    This function builds two graphs by given data,
    using matplotlib.
    '''
    # Unpacking given data
    insertion_1 = []
    insertion_2 = []
    selection_1 = []
    selection_2 = []
    merge_1 = []
    merge_2 = []
    shell_1 = []
    shell_2 = []
    size_of_array = [2**7, 2**8, 2**9, 2**10, 2**11, 2**12, 2**13, 2**14, 2**15]
    for element in data:
        insertion_1.append(element[0][0])
        insertion_2.append(element[0][1])
        selection_1.append(element[1][0])
        selection_2.append(element[1][1])
        merge_1.append(element[2][0])
        merge_2.append(element[2][1])
        shell_1.append(element[3][0])
        shell_2.append(element[3][1])

    # Creating 1-st graph
    experiment_sorting = plt.figure(n)
    plt.xscale('log', basex = 2)
    plt.yscale('log', basey = 10)
    plt.xlabel('Size of array, log2')
    plt.ylabel('Sorting time, sec.')
    plt.plot(size_of_array, insertion_2, label='Insertion sort')
    plt.plot(size_of_array, selection_2, label='Selection sort')
    plt.plot(size_of_array, merge_2, label='Merge sort')
    plt.plot(size_of_array, shell_2, label='Shell sort')
    plt.xticks(size_of_array, list(map(int, list(map(log2, size_of_array)))))
    experiment_sorting.legend(loc='upper center', frameon=True)

    # Creating 2-nd graph
    experiment_comparisons = plt.figure(n+1)
    plt.xscale('log', basex = 2)
    plt.yscale('log', basey = 10)
    plt.xlabel('Size of array, log2')
    plt.ylabel('Comparisons')
    plt.plot(size_of_array, insertion_1, label='Insertion sort')
    plt.plot(size_of_array, selection_1, label='Selection sort')
    plt.plot(size_of_array, merge_1, label='Merge sort')
    plt.plot(size_of_array, shell_1, label='Shell sort')
    plt.xticks(size_of_array, list(map(int, list(map(log2, size_of_array)))))
    experiment_comparisons.legend(loc='upper center', frameon=True)

    return experiment_sorting, experiment_comparisons


if __name__ == "__main__":
    main(0)
