def search(arr):
    for val in arr:
        if val == 1:
            return "HARD"
    return "EASY"


if __name__ == "__main__":
    n = int(input())
    arr = map(int, input().split())
    output = search(arr)
    print(output)
