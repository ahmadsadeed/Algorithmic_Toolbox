from random import seed
from random import randint


def max_pairwise_fast(arr):
    # fast solution O(2n)
    index = 0
    n = len(arr) - 1
    for i in range(1, n):
        if arr[i] > arr[index]:
            index = i
    if arr[index] > arr[n]:
        arr[index], arr[n] = arr[n], arr[index]
    index = 0
    for i in range(1, n - 1):
        if arr[i] > arr[index]:
            index = i
    if arr[index] > arr[n - 1]:
        arr[index], arr[n - 1] = arr[n - 1], arr[index]
    return arr[n - 1] * arr[n]


def max_pairwise_naive(arr):
    # slow solution O(n^2)
    product = 0
    size = len(arr)
    for i in range(size):
        for j in range(i + 1, size):
            product = max(product, arr[i] * arr[j])
    return product


def generate_array(max_size, max_num):
    seed(5)
    rand_size = randint(2, max_size)
    arr = []
    for i in range(rand_size):
        arr.append(randint(0, max_num))
    print('arr:', arr)
    return arr


def stress_test(arr_size, max_num):
    if arr_size > 1:
        arr_test = generate_array(arr_size, max_num)
    else:
        print('Enter size greater than 1. Exiting.')
        exit()
    # print("The array is: ", arr_test)
    product_naive = max_pairwise_naive(arr_test)
    product_fast = max_pairwise_fast(arr_test)
    if product_fast == product_naive:
        print("Ok.", product_naive, product_fast)
    else:
        print("Wrong: ", product_naive, product_fast)


def product_sorting(arr):
    arr.sort()
    n = len(arr) - 1
    print('arr sorted: ', arr)
    return arr[n] * arr[n - 1]


if __name__ == '__main__':
    print("Run Stress Tests:")
    # n = int(input())
    # a = [int(x) for x in input().split()]
    # stress_test(30000, 100)


