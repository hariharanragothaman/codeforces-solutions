def districts_connection(arr, n):
    if len(set(arr)) > 1:
        print('YES')
        for i in range(1, n):
            if arr[i] != arr[0]:
                q = i + 1
                break
        for i in range(1, n):
            if arr[i] != arr[0]:
                print(i+1, 1)
            else:
                print(i+1, q)
    else:
        print('NO')



if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n = int(input())
        arr = list(input().split())
        districts_connection(arr, n)
        i += 1