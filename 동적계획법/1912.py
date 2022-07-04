""" 연속합 """
# 연속된 숫자 중 가장 최대를 고르기

n = int(input())
x1 = list(map(int, input().split()))

x2 = [0] * len(x1)
x2[0] = x1[0]
for i in range(1, n):
    x2[i] = x2[i-1] + x1[i]
    if x1[i] > x2[i]:
        x2[i] = x1[i]
    # 합을 다 더했는데도 안되는 경우
print(max(x2))
