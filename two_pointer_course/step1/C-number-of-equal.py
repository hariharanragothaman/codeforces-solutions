import itertools

def number_of_equal_brute_force(arr1, arr2):
    cnt = 0
    for m in arr1:
        for n in arr2:
            if m == n:
                print(m, n)
                cnt += 1
    print(cnt)

def number_of_equal(arr1, arr2):
    from collections import Counter
    cnt = 0
    hmap1 = Counter(arr1)
    hmap2 = Counter(arr2)
    for k, v in hmap1.items():
        if k in hmap2:
            cnt += v * hmap2[k]
    print(cnt)



if __name__ == '__main__':
    m, n = input().split()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    number_of_equal(arr1, arr2)