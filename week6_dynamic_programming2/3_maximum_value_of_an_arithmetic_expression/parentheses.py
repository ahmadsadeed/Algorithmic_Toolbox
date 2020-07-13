import math


def evaluate(a: int, b: int, op: str):
    if op == '*':
        return a * b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:
        assert 0


def min_max(i, j, op_k, min_matrix, max_matrix):
    p = [math.inf, -math.inf]
    for k in range(i, j):
        a = evaluate(max_matrix[i][k], max_matrix[k + 1][j], op_k[k])
        b = evaluate(max_matrix[i][k], min_matrix[k + 1][j], op_k[k])
        c = evaluate(min_matrix[i][k], max_matrix[k + 1][j], op_k[k])
        d = evaluate(min_matrix[i][k], min_matrix[k + 1][j], op_k[k])
        p[0] = min(p[0], a, b, c, d)
        p[1] = max(p[1], a, b, c, d)
    return p


def get_maximum_value(exp):
    if len(exp) == 0:
        return 0
    # string s = "5-8+7*4-8+9"
    # 200 = (5 − ((8 + 7) × (4 − (8 + 9))))

    # add operators to list
    ops_k = []
    for op in range(1, len(exp), 2):
        ops_k.append(exp[op])
    # Each symbol at an even position of exp string is a digit and
    # at an odd position is one of three operations from {+,-,*}
    size_m = (len(exp) + 1) // 2
    # create the matrix size_m by size_m
    min_matrix = [[0 for _ in range(size_m)] for _ in range(size_m)]
    max_matrix = [[0 for _ in range(size_m)] for _ in range(size_m)]

    # add the digits from exp to diagonal of the matrix
    # this will help later accessing min and max of expressions
    x = 0
    for i in range(size_m):
        min_matrix[i][i] = int(exp[x])
        max_matrix[i][i] = int(exp[x])
        x += 2
    '''
    The main part is here where the min and max of each sub-expression is calculated
    and stored in the matrix. It will look like below:
    
    min_matrix:
    [5, -3, -10, -55, -63,  -94]
    [0,  8,  15,  36, -60, -195]
    [0,  0,   7,  28, -28,  -91]
    [0,  0,   0,   4,  -4,  -13]
    [0,  0,   0,   0,   8,   17]
    [0,  0,   0,   0,   0,    9]
    
    max_matrix:
    [5, -3,  4, 25, 65, 200]
    [0,  8, 15, 60, 52,  75]
    [0,  0,  7, 28, 20,  35]
    [0,  0,  0,  4, -4,   5]
    [0,  0,  0,  0,  8,  17]
    [0,  0,  0,  0,  0,   9]
    '''
    for s in range(1, size_m):
        for i in range(size_m - s):
            j = i + s
            pair = min_max(i, j, ops_k, min_matrix, max_matrix)
            min_matrix[i][j] = pair[0]
            max_matrix[i][j] = pair[1]

    return max_matrix[0][size_m-1]


if __name__ == '__main__':
    print("main():")
    s = "5-8+7*4-8+9"
    print(get_maximum_value(s))

