def find_subsets_same_color(arr, n):
    """
    1. Keep going row-wise
    2. Check if it's the same value - if it's increment by 1
       once it's not the same - replace all values to the same in that row
    3.
      3 5 5 1 2
    3 1 1 1 1 1
    5 X 2 3 3 3
    5 X X 4 4 4
    1 X X X 5 5
    2 X X X X 6

    """
    cnt = 0
    dp = [[0]*(n+1) for i in range(n+1)]

    # Initialize the DP Array
    j = 0
    for i in range(1, n+1):
        dp[0][i] = arr[j]
        j += 1

    k = 0
    for i in range(1, n+1):
        dp[i][0] = arr[k]
        k += 1
    print('The initialized DP is:', dp)

    # Doing the logic.
    for i in range(1, n+1):
        for j in range(i, n+1):
            if dp[0][j]  == dp[i][0]:
                cnt += 1
                dp[i][j] = cnt
            else:
                dp[i][j] = cnt

    print("The final DP matrix is:", dp)
    return cnt

if __name__ == '__main__':
    n = int(input())
    arr = input().split()
    op = find_subsets_same_color(arr, n)
    print(op)

