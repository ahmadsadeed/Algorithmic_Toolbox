def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        # print("Only one element:", a[left])
        return 1
    # write your code here
    a.sort()
    count = 0
    current = -1
    for x in range(right):
        if a[x] == current:
            count += 1
        elif a[x] != current:
            if count > (right / 2):
                return 1
            else:
                count = 1
                current = a[x]

    if count > (right / 2):
        return 1

    return 0


if __name__ == '__main__':
    print("main():")
    arr = []
    major = get_majority_element(arr, 0, len(arr))
    print(major)
