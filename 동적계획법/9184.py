"""신나는 함수 실행"""
# 동적 계획법 이용

import sys
input = sys.stdin.readline

x = [[[0]*21 for _ in range(21)] for _ in range(21)]
# 값을 저장하기 위한 3차원 배열 선언

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    
    # 이미 존재하는 값은 배열에서 뽑기
    if x[a][b][c]:
        return x[a][b][c]
    if a < b < c:
        x[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return x[a][b][c]

    x[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return x[a][b][c]
    
while(True):
    a, b, c = map(int, input().split())    
    if a == -1 & b == -1 & c == -1:
        break
    else: 
        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")