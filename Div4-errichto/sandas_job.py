"""

"""
def gen_permute_iter(arr):
    if len(arr) < 1:
        yield arr
    else:
        for perm in gen_permute_iter(arr[1:]):
            for i in range(len(arr)):
                yield perm[:i] + arr[0:1] + perm[i:]


def sanda_job_check_permutation(a, s):
    s = int(s)
    for c in gen_permute_iter(a):
        if int(c) + int(a) == int(s) and not(str(c).startswith('0')):
            return True
    return False


def sanda_job_without_permutation(a, s):
    b = int(s) - int(a)
    if sorted(str(b)) == sorted(str(a)):
        return True
    return False




if __name__ == '__main__':
    a, s = list(input().split())
    if sanda_job_without_permutation(a, s):
        print('YES')
    else:
        print('NO')