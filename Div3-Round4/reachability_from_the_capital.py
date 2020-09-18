from collections import defaultdict


def topo_sort(graph):
    n = len(graph)
    res, visited = [], [False] * n

    for i in range(n):
        if not visited[i]:
            stack = [i]
            while stack:
                start = stack[-1]
                if not visited[start]:
                    visited[start] = True
                    for child in graph[start]:
                        if not visited[child]:
                            stack.append(child)
                else:
                    res.append(stack.pop())

    return res


if __name__ == '__main__':
    ncities, nroads, capital = map(int, input().split())

    g = [[] for _ in range(ncities)]

    for i in range(nroads):
        u, v = map(int, input().split())
        g[u - 1].append(v - 1)

    print("The graph is:", g)

    print("Calling Topsort")
    op = topo_sort(g)
    print(op)
