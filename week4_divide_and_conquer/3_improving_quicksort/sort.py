import sys
import random


def partition2(a, l, r):
    x = a[l]  # x is our pivot. The l element
    j = l  # copy the index of l to j
    for i in range(l + 1, r + 1):
        # from l+1 to j element is all elements less than x
        # from j+1 to i element is all elements greater than x
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    # swap the pivot x with last element (position j) that is less than x
    a[l], a[j] = a[j], a[l]
    # j is the final position of the pivot a[l]
    return j


# 3 partition helps with repeating elements
def partition3(a, l, r):
    x = a[l]  # x is our pivot. The l element
    j = l  # copy the index of l to j
    j_next = l + 1
    for i in range(l + 1, r + 1):
        # from l+1 to j element is all elements less than x
        # from j+1 to i element is all elements greater than x
        if a[i] <= x:
            # if a[i] <= pivot, j++ and swap it with first number > x
            j += 1
            a[i], a[j] = a[j], a[i]
            if a[j] < x:
                a[j_next], a[j] = a[j], a[j_next]
                j_next += 1

    a[l], a[j_next - 1] = a[j_next - 1], a[l]
    return j_next, j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)  # l + random.randint() % (r - l + 1)
    a[l], a[k] = a[k], a[l]
    pivot = partition3(a, l, r)
    # pivot is in its final position. Sort before and after
    randomized_quick_sort(a, l, pivot[0] - 1)
    randomized_quick_sort(a, pivot[1] + 1, r)


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    # randomized_quick_sort(a, 0, n - 1)
    # for x in a:
    #     print(x, end=' ')
    print("main():")
    arr = [672, 43, 3, 3, 533, 2, 56, 90, 3, 3, 3, 55, 21, 765]
    # print(arr)
    randomized_quick_sort(arr, 0, len(arr) - 1)
    print(arr)
