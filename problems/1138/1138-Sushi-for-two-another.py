def find_continuous_subsegment(arr):
    arr = ''.join(c for c in arr)
    ones = arr.split('2')
    twos = arr.split('1')
    ones = [len(c) for c in ones if c]
    twos = [len(c) for c in twos if c]
    val1, val2 = max(ones), max(twos)
    result = min(val1, val2)
    print(2*result)

if __name__ == '__main__':
    n = int(input())
    arr = list(input().split())
    find_continuous_subsegment(arr)