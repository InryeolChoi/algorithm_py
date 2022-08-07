"""분해합"""

n = int(input())
for i in range(n):
    a = i
    for x in str(i):
        a += int(x)
    
    if a == n:
        print(i)
        break