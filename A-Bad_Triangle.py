from itertools import combinations

test_cases = int(input())

while test_cases > 0:
    n = input()
    print("Entering next test case")
    print("The value of n is:", n)
    arr = input().split()
    arr = [int(c) for c in arr]
    print("The array is:", arr)

    hashmap = {}



    flag = False

    for c in combinations(arr, 3):
        a, b, c = c
        if (a+b < c) or (a+c < b) or (b+c < a):
            result = []
            result.append(arr.index(a)+1)
            result.append(arr.index(b)+1)
            result.append(arr.index(c)+1)
            result = ' '.join(str(c) for c in result)
            print(result)
            flag = True
            break

    if not flag:
        print("-1")


    test_cases -= 1