"""
Given an array of n
integers ai. Let's say that the segment of this array a[l..r] (1≤l≤r≤n) is good
if the sum of elements on this segment is at least s

Your task is to find the shortest good segment.

Input
The first line contains integers n and s (1≤n≤105, 1≤s≤1018). The second line contains integers ai (1≤ai≤109).
Output
Print one integer, the length of the shortest good segment. If there are no such segments, print −1
"""

def shortest_good_segment(arr, target_sum):
    left, right = 0, 0
    wsum = 0
    wlength = float('inf')

    for right in range(len(arr)):
        # this keeps expanding the right window
        wsum += arr[right]
        print(f"The window sum is: {wsum}")
        # Now we want to find the shortest subsegment
        # Contract window if sum is greater than s
        print(f"left is: {left}, right is: {right}")
        while wsum >= target_sum:
            wsum -= arr[left]
            left += 1
            print(f"left is: {left}, right is: {right}")
            print(f"The window sum is: {wsum}")
            if wsum >= target_sum:
                wlength = min(wlength, right - left + 1)

    print(wlength)

def shortest_good_segment_template(arr, target_sum):
    left, right = 0, 0
    wsum = 0
    wlength = float('inf')

    for right in range(len(arr)):
        # this keeps expanding the right window
        wsum += arr[right]
        print(f"The window sum is: {wsum}")
        # Now we want to find the shortest subsegment
        # Contract window if sum is greater than s
        print(f"left is: {left}, right is: {right}")
        while wsum - arr[left] >= target_sum:
            wsum -= arr[left]
            left += 1
            print(f"left is: {left}, right is: {right}")
            print(f"The window sum is: {wsum}")
            if wsum >= target_sum:
                wlength = min(wlength, right - left + 1)

    print(wlength)

if __name__ == '__main__':
    n, target_sum = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    shortest_good_segment_template(arr, target_sum)