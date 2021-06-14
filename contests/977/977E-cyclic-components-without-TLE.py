from collections import defaultdict


def connected_components(graph, n):
    visited = [False] * (n+1)

    cyclic_components = 0

    for i in range(1, n+1):
        if visited[i]:
            continue

        # Setting some defaults:
        cycle_flag = True
        visited[i] = True

        # Applying DFS
        stack = [i]
        while stack:
            node = stack.pop()
            if len(graph[node]) != 2:
                cycle_flag = False
            for nei in graph[node]:
                if visited[nei] == False:
                    visited[nei] = True
                    stack.append(nei)

        cyclic_components += int(cycle_flag)
    print(cyclic_components)



if __name__ == '__main__':
    vertices, edges = list(map(int, input().split()))
    graph = defaultdict(list)
    i = 0
    while i < edges:
        u, v = list(map(int, input().split()))
        graph[u].append(v)
        graph[v].append(u)
        i += 1
    connected_components(graph, vertices)
