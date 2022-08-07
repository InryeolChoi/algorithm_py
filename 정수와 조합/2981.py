"""검문"""
n = int(input())
number, gap = [], []
for _ in range(n):
    number.append(int(input()))
number.sort()

for i in range(1, n):
	gap.append(number[i] - number[i-1])

# 최대공약수 구하기
def find_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def gcd_n(arr):
    gcd = arr[0]
    for item in arr:
        gcd = find_gcd(gcd, item)
    return gcd

x = gcd_n(gap)
ans = []
# 약수 구하기
for i in range(2, x+1):
    if x % i == 0:
        ans.append(i)

for i in ans:
    print(i, end=" ")