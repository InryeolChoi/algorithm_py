""" Z """

import sys
input = sys.stdin.readline

def dc(x, y, n):
    global cnt

    # 박스 안에 있는지 판단
    if r < x or x + n <= r or c < y or y + n <= c:
        cnt += n**2
        return
    
    # 큰 박스 -> 작은 박스로 찾아보기
    if n > 2:
        n //= 2
        dc(x, y, n)
        dc(x, y + n, n)
        dc(x + n, y, n)
        dc(x + n, y + n, n)
    
    # 박스 중 0, 1, 2, 3번째를 찾는 부분
    else:
        if x == r and y == c:
            print(cnt)
        elif x == r and y + 1 == c:
            print(cnt + 1)
        elif x + 1 == r and y == c:
            print(cnt + 2)
        else:
            print(cnt + 3)
        sys.exit()


cnt = 0        
n, r, c = map(int,input().split())
dc(0, 0, 2**n)
