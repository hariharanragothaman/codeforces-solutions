import bisect


def longest_increasing_subsequence(arr):
    temp = []
    for n in arr:
        index = bisect.bisect_left(temp, n)
        if index == len(temp):
            if not temp or (temp[-1] + 1 == n):
                temp.append(n)
        # else:
        #     temp[index] = n
        # print(f"The temp is: {temp}")
    return temp


if __name__ == "__main__":
    n = int(input())
    arr  = list(map(int, input().split()))
    result = longest_increasing_subsequence(arr)
    print(len(result))
    # print(result)
    op = [arr.index(c)+1 for c in result]
    print(*op)