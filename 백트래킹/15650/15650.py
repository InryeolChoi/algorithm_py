"""n과 m - (2)"""
n, m = list(map(int, input().split()))
graph = []

def dfs(graph):
    if len(graph) == m:
        print(" ".join(map(str, graph)))
        return

    for i in range(n):
        if i in graph:
            continue
        graph.append(i)
        dfs()
        graph.pop()

dfs(graph)