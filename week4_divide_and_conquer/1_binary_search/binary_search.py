def binary_search(a, x):
    left = 0
    right = len(a) - 1
    while left <= right:
        mid = int(left + (right - left) / 2)
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    print("main(): ")
    arr = [2, 3, 43, 64, 66, 70, 77, 99]
    num = 99
    index = binary_search(arr, num)
    print("index: ", index)
