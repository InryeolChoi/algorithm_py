"""인간 컴퓨터 상호작용"""
import sys
input = sys.stdin.readline

S = list(input().rstrip()) # 문자열
arr = [[0 for i in range(26)] for _ in range(len(S))]

for i in range(len(S)):
    arr[i][ord(S[i]) - 97] = 1
    for j in range(26):
        arr[i][j] += arr[i-1][j]

for i in range(len(S)):
    print(arr[i])

q = int(input()) # 문제의 수
for _ in range(q):
    alpha, l, r = input().split()
    alpha = ord(alpha) - 97
    l, r = int(l), int(r)
    if l == 0:
        print(arr[r][alpha])
    else:
        print(arr[r][alpha] - arr[l-1][alpha])