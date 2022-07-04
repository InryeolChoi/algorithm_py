"""인간 컴퓨터 상호작용"""
import sys
input = sys.stdin.readline

S = input() # 문자열 
q = int(input()) # 문제의 수
for _ in range(q):
    alpha, l, r = map(str, input().split())
    l, r = int(l), int(r)
    cnt = [0] * len(S)
    for i in range(r+1):
        if S[i] == alpha:
            cnt[i] = cnt[i-1] + 1
        else: cnt[i] = cnt[i-1]
    
    print(cnt[r] - cnt[l-1])