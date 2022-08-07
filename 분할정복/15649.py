"""n과 m - (1)"""
n, m = list(map(int, input().split()))
graph = []

def dfs():
    if len(graph) == m:
        print(" ".join(map(str, graph)))
        return
    
    for i in range(1, n+1):
        if i in graph:
            continue
        graph.append(i)
        dfs()
        graph.pop()
        
dfs()
