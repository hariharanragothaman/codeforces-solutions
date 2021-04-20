from collections import defaultdict

alpha = [chr(c) for c in range(ord('a'), ord('z') + 1)]


def string_equality(s1, s2, k):
    s1_map = defaultdict(int)
    s2_map = defaultdict(int)

    # Calculating the count
    for s in s1:
        s1_map[s] += 1
    for s in s2:
        s2_map[s] += 1

    for c in alpha:
        while s1_map[c] > s2_map[c]:
            s1_map[c] -= k
            s1_map[chr(ord(c)+1)] += k

    for c in list(s1_map) + list(s2_map):
        if s1_map[c] != s2_map[c]:
            print('No')
            break
    else:
        print('Yes')


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n, k = map(int, input().split())
        a = input()
        b = input()
        string_equality(a, b, k)
        i += 1