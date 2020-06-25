def gcd_fast(a, b):
    big = max(a, b)
    small = min(a, b)
    remain = big % small

    while remain != 0:
        big = small
        small = remain
        remain = big % small

    return small


def lcm_fast(a, b):
    gcd = gcd_fast(a, b)
    return (a * b) / gcd


if __name__ == '__main__':
    print('Main: ')
    # print(gcd_fast(28851538, 1183019))
