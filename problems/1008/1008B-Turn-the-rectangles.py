def turn_the_rectangles():
    n = int(input())
    i = 0
    arr = []
    w = h = float('inf')
    while i < n:
        wi, hei = list(map(int, input().split()))

        if hei <= h:
            w, h = wi, hei

        elif hei > h:
            # See if it's possible to rotate
            if wi <= h:
                # Swap
                wi, hei = hei, wi
                # Reassign
                w, h = wi, hei
            elif wi > h:
                print('NO')
                exit()
        i += 1
    print('YES')

def turn_the_rectangles_perfect():
    n = int(input())
    width, height = map(int, input().split())
    stack = [max(width, height)]

    flag = True

    for i in range(n-1):
        width, height = map(int, input().split())
        ma = max(width, height)
        mi = min(width, height)

        if ma <= stack[-1]:
            stack.append(ma)
        elif mi <= stack[-1]:
            stack.append(mi)
        else:
            flag = False

    if flag:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    turn_the_rectangles_perfect()


