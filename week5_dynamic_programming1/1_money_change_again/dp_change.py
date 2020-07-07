import math


def get_change(m):
    # 1, 3, 4
    # the greedy way
    a = int((m / 4) + ((m % 4) / 3) + ((m % 4) % 3))
    b = int(((m / 4) - 1) + (m - ((m / 4) - 1) * 4) / 3 +
            (m - ((m / 4) - 1) * 4) % 3)
    return min(a, b)


def dp_change(m):
    denominations = [1, 3, 4]
    arr = [math.inf] * m
    arr.insert(0, 0)
    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # [0, 1, 2, 1, 1, 2, 2, 2, 2, 3,  3]
    for i in range(1, m + 1):
        for den in denominations:
            if i >= den:
                coins = arr[i - den] + 1
                if coins < arr[i]:
                    arr[i] = coins
    return arr[m]


if __name__ == '__main__':
    num = 6
    print(get_change(num))
    print(dp_change(num))
