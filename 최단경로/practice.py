import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())

graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)
for _ in range(n):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start)) # 시작노드 정보 우선순위 큐에 삽입
    distance[start] = 0 # 시작노드 -> 시작
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print("도달 불가")
    else:
        print(distance[i])