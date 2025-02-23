"""수열"""
n, k = map(int, input().split())
celcius = list(map(int, input().split()))
cumsum = [0] * (n-k+1)

for i in range(k):
    cumsum[0] += celcius[i]

for i in range(1, n-k+1):
    old = celcius[i-1]
    new = celcius[i+k-1]
    cumsum[i] = cumsum[i-1] + new - old
print(max(cumsum))