def fibonacci_fast(num):
    if num <= 1:
        return num
    array = list()
    array.append(0)
    array.append(1)

    for i in range(2, num + 1):
        array.insert(i, array[i - 1] + array[i - 2])
    return array[num]


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for i in range(n - 1):
        tmp_previous = previous
        previous = current
        current = tmp_previous + current
    return current % 10


def fibonacci_last_digit_fast(n):
    if n <= 1:
        return n
    array = list()
    array.append(0)
    array.append(1)

    for i in range(2, n + 1):
        array.insert(i, (array[i - 1] + array[i - 2]) % 10)
    return array[n]


if __name__ == '__main__':
    print('Main: ')
    # print(fibonacci_fast(327305))
    print(fibonacci_last_digit_fast(327305))
