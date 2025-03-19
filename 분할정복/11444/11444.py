""" 피보나치 수 6 """
import sys
input = sys.stdin.readline

def multiply(A, B):
    n = len(A)
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):

            # temp[i][j]
            for k in range(2):
                temp[i][j] += (A[i][k] * B[k][j]) % 1000000007
    return temp

def power(A, n):
    if n == 1:
        return A
    
    if n % 2 == 0:
        temp = power(A, n//2)
        return multiply(temp, temp)
    
    else:
        temp = power(A, n-1)
        return multiply(temp, A)


def mat_vec(A):
    ans = []
    x = [1, 0]
    for i in range(2):
        temp = 0
        for j in range(2):
            temp += (A[i][j] * x[j]) % 1000000007
        ans.append(temp)
    return ans


if __name__ == "__main__":
    n = int(input())
    A = [[1, 1], [1, 0]]
    if n == 0:
        print(0)
    else:
        A = power(A, n)
        ans = mat_vec(A)
        print(ans[1])