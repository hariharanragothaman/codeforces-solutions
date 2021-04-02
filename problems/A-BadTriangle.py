test_cases = int(input())

while test_cases > 0:
    n = input()
    print("Entering next test case")
    print("The value of n is:", n)
    arr = input().split()
    arr = [int(c) for c in arr]
    print("The array is:", arr)

    i = 0
    flag = False
    while i < len(arr)-2:
        if (arr[i] + arr[i+1] < arr[i+2]) or (arr[i+1] + arr[i+2] < arr[i]) or (arr[i+2] + arr[i] < arr[i+1]):
            result = []
            result.append(i+1)
            result.append(i+2)
            result.append(i+3)
            result = ' '.join(str(c) for c in result)
            print(result)
            flag = True
            break
        i += 1

    if not flag:
        print("-1")

    test_cases -= 1