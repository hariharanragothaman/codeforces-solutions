def make_divisible(a, b):
    moves = 0
    while a % b != 0:
        a += 1
        moves += 1
    return moves

def make_div_eff(a,b):
    if a % b == 0:
        return 0
    else:
        return b - (a%b)

if __name__ == '__main__':
    t = int(input())
    while t > 0:
        inp = input().split()
        inp = [int(c) for c in inp]
        a, b = inp[0], inp[1]
        res = make_div_eff(a, b)
        print(res)
        t -= 1