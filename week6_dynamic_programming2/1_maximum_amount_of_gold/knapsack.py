def optimal_weight(capacity, data):
    col = capacity + 1  # weights
    row = len(data) + 1  # values

    matrix = [[0 for n in range(0, col)] for i in range(0, row)]
    # for i in range(1, row):
    #     matrix.append([0] * col)

    for r in range(1, row):
        for c in range(1, col):
            matrix[r][c] = matrix[r - 1][c]
            if data[r - 1] <= c:
                val = (matrix[r - 1][c - data[r - 1]]) + data[r - 1]
                if matrix[r][c] < val:
                    matrix[r][c] = val

    return matrix[row - 1][col - 1]


if __name__ == '__main__':
    print("main:")
    arr = [1, 4, 8]
    W = 10
    print(optimal_weight(W, arr))
