from collections import deque


def neighbours(r, c, R, C):
    for rows, cols in( (r-1, c), (r, c-1), (r+1, c), (r, c+1)):
        if 0 <= rows < R and 0 <= cols < C:
            yield rows, cols

def protect_the_sheep(matrix, R, C):
    """
    Note: Wolves can't move diagonally
         Sheeps and dog stay in place
         no wolf can enter a cell with a dog
    Approach: Find where all the sheep are there

    We need not minimize the number? -- HMMM That makes it a little simple

    Basic Cases: If the wolf is next to the sheep then you cannot save it.
        So we need to know neighbours of the sheep
    :param matrix:
    :param r:
    :param c:
    :return:
    """
    q = deque()
    for i, row in enumerate(matrix):
        for c, val in enumerate(row):
            if val == 'W':
                q.append((i, c))
    #print("The wolf locations are:", q)

    while q:
        i, j = q.popleft()
        for nei in neighbours(i, j, R, C):
            #print("The neighbours are:", nei)
            nr, nc  = nei
            if matrix[nr][nc] == 'S':
                print('No')
                exit()
            elif matrix[nr][nc] == '.':
                matrix[nr][nc] = 'D'

    print('Yes')
    for row in matrix:
        print(''.join(row))




if __name__ == '__main__':
    r, c = map(int, input().split())
    i = 0
    matrix = []
    while i < r:
        rows = [c for c in input()]
        matrix.append(rows)
        i += 1
    #print(matrix)
    protect_the_sheep(matrix, r, c)