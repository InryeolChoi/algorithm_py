"""다이얼"""
word = list(input())
arr, sum = [], 0

for w in word:
    n = ord(w) - 65
    if n < 18:
        arr.append(n // 3 + 2)
    else:
        if n == 18: arr.append(7)
        if 19 <= n <= 21: arr.append(8)
        if 22 <= n <= 25: arr.append(9)

for a in arr:
    sum += (a + 1)
print(sum)
