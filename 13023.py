"""ABCDE"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False] * 2000
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# dfs
def dfs(start, depth):
    global ans
    visited[start] = True

    if depth == 4:
        ans = True
        return

    for i in graph[start]:
        if not visited[i]:
            visited[i] = True

            dfs(i, depth + 1)
            visited[i] = False

for i in range(n):
    dfs(i, 0)
    visited[i] = False
    if ans: break
if ans: print(1)
else: print(0)