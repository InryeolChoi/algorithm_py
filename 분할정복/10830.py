""" 행렬 제곱 """
import sys
input = sys.stdin.readline

def multiply(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):  
            # c[i][j]의 값 구하기
            for k in range(n):
                C[i][j] += (A[i][k] * B[k][j]) % 1000
    return C

def power(A, n):
    # 지수가 1인 경우
    if n == 1:
        return A

    # 지수가 짝수인 경우
    if n % 2 == 0:
        temp = power(A, n//2)
        return multiply(temp, temp)

    # 지수가 홀수인 경우
    else:
        temp = power(A, n-1)
        return multiply(temp, A)

if __name__ == "__main__":
    n, b = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(n)] 
    ans = power(A, b)
    
    for i in range(n):
        for j in range(n):
            print(ans[i][j] % 1000, end=" ")

        print("")
