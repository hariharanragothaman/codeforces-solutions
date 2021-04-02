def merge_arrays_normal(nums1, nums2):
    nums1[:] = sorted(nums1 + nums2)
    return nums1

def merge_arrays(nums1, nums2):
    i, j = 0, 0
    res = []
    while i < len(nums1) or j < len(nums2):
        if (i < len(nums1) and nums1[i] < nums2[j]) or (j == len(nums2)):
            res.append(nums1[i])
            i += 1
        else:
            res.append(nums2[j])
            j += 1
    return res

if __name__ == '__main__':
    m, n = input().split()
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    result = merge_arrays_normal(arr1, arr2)
    print(*result)