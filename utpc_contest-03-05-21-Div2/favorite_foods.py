
if __name__ == '__main__':
    n = int(input())
    i = 0
    hmap = {}
    while i < n:
        f, r = list(input().split())
        hmap[f] = int(r)
        i += 1
    hmap = {k:v for k, v in sorted(hmap.items(), key= lambda x:x[1])}
    keys = list(hmap.keys())
    print(keys[0], keys[-1])