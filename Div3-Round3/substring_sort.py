"""
You are given n strings. Each string consists of lowercase English letters.
Rearrange (reorder) the given strings in such a way that for every string, all strings that are placed before it are its substrings.
"""

def check_substr(a, b):
    if a in b:
        return True
    else:
        return False

def substring_sort(strings):
    #print("The strings are:", *strings)
    strings_new = set(strings)
    strings_new = sorted(strings, key=len)
    #print(strings_new)

    i = len(strings_new)-2
    while i >= 0:
        result = check_substr(strings_new[i], strings_new[i+1])
        if not result:
            print('NO')
            return
        i -= 1

    # Need to print the strings in the same sorted order
    print('YES')
    res = sorted(strings, key=len)
    for c in res:
        print(c)


if __name__ == '__main__':
    n = int(input())
    strs = []
    while n > 0:
        inp_str = input()
        strs.append(inp_str)
        n -= 1
    substring_sort(strs)
