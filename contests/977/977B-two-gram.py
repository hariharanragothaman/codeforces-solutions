def find_substring_max_occurances_fixed_length(s, k):
    from collections import defaultdict
    hmap = defaultdict(int)
    for length in range(2, 3):
        for i in range(0, n-length+1):
            string = s[i:i+length]
            hmap[string] += 1
    print(hmap)

    mx = max(hmap.values())
    for k,v in hmap.items():
        if v == mx:
            return k


if __name__ == '__main__':
    n = int(input())
    s = input()
    result = find_substring_max_occurances_fixed_length(s,2)
    print(result)