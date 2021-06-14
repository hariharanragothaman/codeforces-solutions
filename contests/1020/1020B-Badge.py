
def badge(arr, n):
    """ DFS approach to check if we visit a node twice"""

    # Constructing the graph
    hmap = {}
    for i, c in enumerate(arr, 1):
        hmap[i] = c
    #print("The hashmap is:", hmap)

    result = []

    for i in range(1, n+1):

        #print("The start value now is:", i)
        # The DFS routine
        # Constructing the visited_cnt map
        nodes = list(range(1, n + 1))
        cnt = [0] * n
        cnt_map = dict(zip(nodes, cnt))
        #print("The initial count map is:", cnt_map)

        start = i

        fl = False

        while start in hmap:
            cnt_map[start] += 1
            if cnt_map[start] == 2:
                #print("The value we care for this is:" ,start)
                result.append(start)
                fl = True
                break
            start = hmap[start]

            #print("The cnt map is:", cnt_map)

        if not fl:
            result.append(i)
        #print("*"*10)

    print(*result)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    badge(arr, n)