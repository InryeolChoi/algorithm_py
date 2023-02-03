"""최단경로"""
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())

# 그래프 
graph = [[] for _ in range(v+1)]
distance = [INF] * (v+1)
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(k)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])