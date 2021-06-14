
def vanya_and_fence(h, heights):
    cnt = 0
    for c in heights:
        if c > h:
            cnt += 2
        if c <= h:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    n, h = list(map(int, input().split()))
    heights = list(map(int, input().split()))
    vanya_and_fence(h, heights)