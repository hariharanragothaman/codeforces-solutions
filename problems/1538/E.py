from collections import defaultdict

p = 31
m = 10 ** 9 + 9


def compute_hash(s):
    n = len(s)
    power_mod = [1]
    for i in range(n):
        power_mod.append((power_mod[-1] * p) % m)

    hash_values = [0] * (n + 1)

    for i in range(n):
        hash_values[i + 1] = (hash_values[i] + (ord(s[i]) - ord('a') + 1) * power_mod[i]) % m


def count_occurences(text, pattern):
    text_length = len(text)
    pattern_length = len(pattern)

    power_mod = [1]
    for i in range(text_length):
        power_mod.append((power_mod[-1] * p) % m)

    hash_values = [0] * (text_length + 1)

    for i in range(text_length):
        hash_values[i + 1] = (hash_values[i] + (ord(text[i]) - ord('a') + 1) * power_mod[i]) % m

    pattern_hash = 0
    for i in range(pattern_length):
        pattern_hash += ((ord(pattern[i]) - ord('a') + 1) * power_mod[i]) % m

    occurences = []

    i = 0
    while i + pattern_length - 1 < text_length:
        field_hash = (hash_values[i + pattern_length] - hash_values[i] + m) % m
        if field_hash == pattern_hash * power_mod[i] % m:
            occurences.append(i)
        i += 1

    if occurences:
        return len(occurences)
    else:
        return 0


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        # For each test case
        n = int(input())
        j = 0
        hmap = defaultdict(str)
        last = None
        while j < n:
            ops = input()
            if ':=' in ops:
                k, v = ops.split(':=')
                if k: k = str(k).rstrip()
                if v: v = str(v).lstrip()
                hmap[k] = v
                last = v

            elif '=' in ops:
                left, right = ops.split('=')
                if left:
                    left = str(left).rstrip()
                    left = str(left).lstrip()

                if right:
                    oper1, oper2 = right.split('+')
                    if oper1:
                        oper1 = str(oper1).lstrip()
                        oper1 = str(oper1).rstrip()
                    if oper2:
                        oper2 = str(oper2).lstrip()
                        oper2 = str(oper2).rstrip()

                hmap[left] = hmap[oper1] + hmap[oper2]
                last = hmap[left]
            j += 1

        result = count_occurences(last, pattern='haha')
        print(result)
        i += 1