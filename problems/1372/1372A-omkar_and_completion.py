
def find_complete_array(n):
    return [1] * n


if __name__ == '__main__':
    t = int(input())
    i = 0
    while i < t:
        n = int(input())
        res = find_complete_array(n)
        print(*res)
        i += 1