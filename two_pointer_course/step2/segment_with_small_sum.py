# Classic sliding window problem

"""
Given an array of n integers ai. Let's say that the segment of this array a[l..r] (1≤l≤r≤n) is good
if the sum of elements on this segment is at most s
Your task is to find the longest good segment.

Input

The first line contains integers n and s (1≤n≤105, 1≤s≤1018). The second line contains integers ai (1≤ai≤109).
Output
Print one integer, the length of the longest good segment. If there are no such segments, print 0
"""

def find_longest_good_segment(arr, s):
    """
    This function basically finds longest segment where sum is not greater than s
    :param arr:
    :param s:
    :return:
    """
    left, right = 0, 0
    wsum = 0
    wlength = 0

    for right in range(len(arr)):
        # Here the right window keeps expanding
        wsum += arr[right]
        while wsum > s:
            # here we are contracting the window to ensure, sum is not greater than s
            wsum -= arr[left]
            left += 1
        # To find the max-length - we just use max on the available good segments
        wlength = max(wlength, right-left+1)
    print(wlength)

if __name__ == '__main__':
    n, target_sum = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    find_longest_good_segment(arr, target_sum)