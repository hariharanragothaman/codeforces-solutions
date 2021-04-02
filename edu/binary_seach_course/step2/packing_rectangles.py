from bisect import bisect_left, bisect_right

def find_min_square_size(w, h, n):
    count = 0
    area = w * h
    # Since there are n rectangle total area is:
    total_area = area * n
    print("The total are is:", total_area)
    # Now we need to find, the minimum square area ->  tarea >= (a**2)
    space = [c**2 for c in range(1, int(pow(total_area, 0.5)) + 5 )]
    print("The total space is:", space)


if __name__ == '__main__':
    w, h, n = list(map(int, input().split()))
    op = find_min_square_size(w, h, n)
    print(op)