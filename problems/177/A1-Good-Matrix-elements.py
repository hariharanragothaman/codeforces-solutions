from collections import defaultdict

def get_right_diagonals(arr):
    rows = len(arr)
    hashmap = {}
    for i in range(rows):
        hashmap[(rows-1-i, i)] = arr[rows-1-i][i]
    return hashmap

def get_left_diagonals(arr):
    rows = len(arr)
    hashmap = {}
    for i in range(rows):
        hashmap[(i, i)] = arr[i][i]
    return hashmap

def get_middle_row(arr):
    rows = len(arr)
    mid = rows // 2
    hashmap = {}
    for i in range(n):
        hashmap[(mid, i)] = arr[mid][i]
    return hashmap

def get_middle_column(arr):
    rows = len(arr)
    mid = rows // 2
    hashmap = {}
    for i in range(n):
        hashmap[(i, mid)] = arr[i][mid]
    return hashmap

def good_matrix_elements(A):
    # number of rows and column will be odd - that is a given assumption
    # n x n matrix
    leftDiagonal = get_left_diagonals(A)
    rightDiagonal = get_right_diagonals(A)
    middleRow = get_middle_row(A)
    middleColumn = get_middle_column(A)
    result = defaultdict(int)
    for k, v in leftDiagonal.items():
        if k not in result:
            result[k] = v
    for k, v in rightDiagonal.items():
        if k not in result:
            result[k] = v
    for k, v in middleColumn.items():
        if k not in result:
            result[k] = v
    for k, v in middleRow.items():
        if k not in result:
            result[k] = v
    print(sum(result.values()))

if __name__ == '__main__':
    n = int(input())
    i = 0
    arr = []
    while i < n:
        tmp = list(map(int, input().split()))
        arr.append(tmp)
        i += 1
    good_matrix_elements(arr)