def optimal_summands(num_prize):
    summands = []
    remaining = num_prize

    for x in range(1, num_prize + 1):
        if remaining >= x:
            if (remaining - x) > x:
                summands.append(x)
                remaining -= x
            else:
                summands.append(remaining)
                remaining = 0
        else:
            break
    return summands


if __name__ == '__main__':
    print("Main:")
    n = 100
    summands = optimal_summands(n)
    print(len(summands))
    for i in summands:
        print("{} ".format(i), end='')
