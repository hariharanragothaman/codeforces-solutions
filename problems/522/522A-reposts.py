from collections import defaultdict, deque


def find_popularity(hmap):
    """
    Basically we have to level-order-traversal of an n-array tree
    :param hmap:
    :return:
    """
    q = deque(['polycarp'])

    traverse = []
    level = 0

    while q:
        traverse.append([])
        for i in range(len(q)):
            node = q.popleft()
            traverse[level].append(node)
            for nei in hmap[node]:
                q.append(nei)

        level += 1
    print(traverse)
    print(len(traverse))





if __name__ == '__main__':
    n = int(input())
    hmap = defaultdict(list)
    while n > 0:
        a, b, c = input().split()
        hmap[c.lower()].append(a.lower())
        n -= 1
    find_popularity(hmap)
