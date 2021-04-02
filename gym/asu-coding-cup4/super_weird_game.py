from collections import defaultdict


def find_pairs(nums, k):
    hashmap = defaultdict(list)
    for i in range(len(nums)):
        hashmap[nums[i]].append(i)

    cnt = 0

    for i in range(len(nums)):
        diff = k - nums[i]
        if diff in hashmap:
            values = [c for c in hashmap[diff] if c < i]
            cnt += len(values)

    return cnt



if __name__ == '__main__':
    n, k = list(map(int, input().split()))
    m_nums = list(map(int, input().split()))
    b_nums = list(map(int, input().split()))

    if find_pairs(m_nums, k) < find_pairs(b_nums, k):
        print('BASHAR')
    elif find_pairs(m_nums, k) > find_pairs(b_nums, k):
        print("MAHMOUD")
    else:
        print("DRAW")