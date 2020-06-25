def fibonacci_naive(num):
    if num <= 1:
        return num
    return fibonacci_naive(num - 1) + fibonacci_naive(num - 2)


def fibonacci_fast(num):
    if num <= 1:
        return num
    array = list()
    array.append(0)
    array.append(1)

    for i in range(2, num + 1):
        array.insert(i, array[i - 1] + array[i - 2])
    return array[num]


def test_solution():
    assert (fibonacci_fast(3) == 2)
    assert (fibonacci_fast(10) == 55)
    for i in range(20):
        assert (fibonacci_fast(i) == fibonacci_naive(i))


if __name__ == '__main__':
    print('main: ')
    # n = input()
    print(fibonacci_naive(10))
    # print(fibonacci_fast(10))
    # test_solution()
