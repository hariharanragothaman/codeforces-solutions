
def string_equality(s1, s2, k):
    if s1 == s2:
        return True
    

if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n, k = map(int, input().split())
        a = input()
        b = input()
        string_equality(a, b, k)
        i += 1