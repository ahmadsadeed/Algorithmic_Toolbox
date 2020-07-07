
def optimal_sequence(n):
    # +1, times(2), times(3)
    ops = [0, 1]
    for x in range(2, n + 1):
        prev = ops[x - 1]
        mins = [prev]
        if x % 2 == 0:
            remain = int(x / 2)
            min1 = ops[remain]
            mins.append(min1)
        if x % 3 == 0:
            remain = int(x / 3)
            min2 = ops[remain]
            mins.append(min2)

        z = min(mins)
        ops.append(z + 1)

    print("ops: ", ops)
    sequence = []
    while n > 0:
        sequence.append(int(n))
        if n % 2 != 0 and n % 3 != 0:
            n -= 1
        elif n % 2 == 0 and n % 3 == 0:
            n /= 3
        elif n % 2 == 0:
            if ops[int(n - 1)] < ops[int(n / 2)]:
                n -= 1
            else:
                n /= 2
        elif n % 3 == 0:
            if ops[int(n - 1)] < ops[int(n / 3)]:
                n -= 1
            else:
                n /= 3

    sequence.reverse()
    return sequence


if __name__ == '__main__':
    print("Main()")
    m = 10
    seq = optimal_sequence(m)
    print(len(seq) - 1)
    print("seq: ", seq)
