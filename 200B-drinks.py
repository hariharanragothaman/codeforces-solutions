def orange_in_cocktail(arr, n):
    return sum(arr) / n

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = orange_in_cocktail(arr, n)
    print(result)