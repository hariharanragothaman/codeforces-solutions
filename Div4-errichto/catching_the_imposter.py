
def can_find_impostor(arr, n, k):
    arr = sorted(set(arr))
    total = list(range(1 ,n+1))
    imposters = [c for c in total if c not in arr]
    if imposters and len(imposters) == 1:
        return True
    return False

if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    if can_find_impostor(arr, n, k):
        print('YES')
    else:
        print('NO')