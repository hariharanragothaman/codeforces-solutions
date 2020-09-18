from collections import defaultdict

def topo_sort_variant(graph, n):
    print("IN top-sort function")
    result = []
    visited = [False] * (n+1)

    for i in range(1, n+1):
        print("The node under consideration", i)
        if not visited[i]:
            stack = [i]
            print("The stack is", stack)
            while stack:
                node = stack[-1]
                if not visited[node]:
                    visited[node] = True
                    for child in graph[node]:
                        if not visited[child]:
                            stack.append(child)
                    print("The updated stack is", stack)

                else:
                    result.append(stack.pop())
                print("The result is:", result)
                print("****************************************")
    return result



if __name__ == '__main__':
    min_roads_required = 0
    ncities, nroads, capital = map(int, input().split())

    g = defaultdict(list)

    for i in range(nroads):
        u, v = map(int, input().split())
        g[u].append(v)

    print("The graph is:", g)
    op = topo_sort_variant(g, ncities)
    print("The topo sort output is", op)

    visited = [False] * (ncities + 1)

    def topo_dfs(i):
        stack = [i]
        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                for child in g[node]:
                    if not visited[child]:
                        stack.append(child)
            else:
                stack.pop()


    topo_dfs(capital)

    print("After doing initial DFS", visited)

    print("Going to check sorted output")
    for i in reversed(topo_sort_variant(g, ncities)):
        if not visited[i]:
            print("These are not visited", i)
            topo_dfs(i)
            print("The updated visited is:", visited )
            min_roads_required += 1
        print("********************************")
    print(min_roads_required)