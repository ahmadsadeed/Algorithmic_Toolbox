def change(m):
    return int(m / 10) + int((m % 10) / 5) + int((m % 10) % 5)


if __name__ == '__main__':
    num = 8
    print('Change: ', change(num))