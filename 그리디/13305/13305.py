"""도로와 연료"""
# 그리디 알고리즘

n = int(input())
line = list(map(int, input().split()))
prices = list(map(int, input().split()))

sum = 0
min = prices[0]
for i in range(n-1):
    if prices[i] < min:
        min = prices[i] # 최소 비용 찾기
    sum += min * line[i] # (최소 비용) * 거리
print(sum)