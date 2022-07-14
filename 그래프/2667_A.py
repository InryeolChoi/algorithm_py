"""단자번호붙이기"""
import sys
input = sys.stdin.readline

n = int(input())

graph = []      # 입력받을 그래프를 담을 리스트 선언
village = []    # 결과를 담을 리스트(마을) 선언
count = 0

for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 한 점을 기준으로 한칸 씩 이동할 좌표 설정
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# dfs
def dfs(x, y):
    global count

    # x, y 값 조정
    if x < 0 or x >= n or y < 0 or y >= n:
        return

    # 그래프 값이 1일 경우 count 측정하기
    if graph[x][y] == 1:
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)

# 그래프의 원소가 1일때만 dfs로 집을 방문한다.
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            dfs(i, j)
            village.append(count)
            count = 0

village.sort()       # 오름차순으로 정렬

print(len(village))  # 총 단지수 출력
for k in village:    # 각 단지마다 집의 수 출력
    print(k)


