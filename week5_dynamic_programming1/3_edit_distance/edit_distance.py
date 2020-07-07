
def edit_distance(str1, str2):
    len1 = len(str1) + 1
    len2 = len(str2) + 1

    ''' For example, if str1 = 'editing' and str2 = 'distance', 
        create matrix like below:
    [0, 1, 2, 3, 4, 5, 6, 7, 8]
    [1, 0, 0, 0, 0, 0, 0, 0, 0]
    [2, 0, 0, 0, 0, 0, 0, 0, 0]
    [3, 0, 0, 0, 0, 0, 0, 0, 0]
    [4, 0, 0, 0, 0, 0, 0, 0, 0]
    [5, 0, 0, 0, 0, 0, 0, 0, 0]
    [6, 0, 0, 0, 0, 0, 0, 0, 0]
    [7, 0, 0, 0, 0, 0, 0, 0, 0]
    '''
    matrix = [[n for n in range(0, len2)]]
    for i in range(1, len1):
        matrix.append([i] + ([0] * (len2 - 1)))

    for y in range(1, len2):
        for x in range(1, len1):
            insertion = (matrix[x][y-1]) + 1
            deletion = (matrix[x-1][y]) + 1
            match = matrix[x-1][y-1]
            mismatch = (matrix[x-1][y-1]) + 1
            if str1[x - 1] == str2[y - 1]:
                matrix[x][y] = min(insertion, deletion, match)
            else:
                matrix[x][y] = min(insertion, deletion, mismatch)

    return matrix[len1-1][len2-1]


if __name__ == '__main__':
    print("main()")
    s1 = 'editing'
    s2 = 'distance'
    print(edit_distance(s1, s2))
