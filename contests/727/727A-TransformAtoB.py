from collections import deque
from collections import defaultdict


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def is_transform_possible(start, end):
    cnt, path = 0, []
    if start == end:
        return cnt, []

    hmap = defaultdict(list)
    flag = False

    q = deque([a])
    while q:
        node = q.popleft()
        if node > (2*end):
            break

        child1 = node*2
        child2 = int(str(node)+'1')


        if child1 <= end:
            hmap[node].append(child1)
            q.append(child1)

        if child2 <= end:
            hmap[node].append(child2)
            q.append(child2)

        if child1 == end or child2 == end:
            flag = True
            break

    if flag:
        path = find_shortest_path(hmap, a, b)
        return len(path), path
    else:
        return 0, []

if __name__ == '__main__':
    a, b = map(int, input().split())
    tcnt, arr = is_transform_possible(a, b)
    if tcnt:
        print('YES')
        print(tcnt)
        print(*arr)
    else:
        print('NO')
