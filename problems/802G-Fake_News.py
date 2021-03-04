substring = 'heidi'
input_string = input()

def subsequence(s, t):
    for i in range(len(s)):
        try:
            idx = t.index(s[i])
        except:
            return "NO"
        t = t[idx+1:]
    return "YES"

res = subsequence(substring, input_string)
print(res)

