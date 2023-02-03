"""특정한 최단경로"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
v1, v2 = map(int, input().split())

def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist: continue
        for next in graph[node]:
            cost = distance[node] + 1
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
    return distance

case1, case2 = 0, 0
s_v1 = dijkstra(1)[v1]
s_v2 = dijkstra(1)[v2]
v1_v2 = dijkstra(v1)[v2]
v1_n = dijkstra(v1)[n]
v2_n = dijkstra(v2)[n]

case1 = s_v1 + v1_v2 + v2_n
case2 = s_v2 + v1_v2 + v1_n
print(min(case1, case2))