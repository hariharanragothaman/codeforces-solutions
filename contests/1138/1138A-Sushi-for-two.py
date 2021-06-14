def find_continuous_subsegment(arr):
    temp = []

    cnt, prev = 1, arr[0]
    for i in range(n - 1):
        print("The value of i is:", i)
        if arr[i + 1] == prev:
            cnt += 1
        else:
            temp.append(cnt)
            print("The count is:", cnt)
            cnt = 1

        prev = arr[i + 1]


    print("The count is:", cnt)
    temp.append(cnt)

    print("The temp is:", temp)
    print("The prev is:", prev)

    res = 0
    for i in range(len(temp) - 1):
        res = max(res, 2 * min(temp[i], temp[i + 1]))
    print(res)


if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())
    find_continuous_subsegment(arr)