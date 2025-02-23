"""벌집"""

x = int(input())
sum, i = 1, 0
while(1):
    sum += 6 * i
    if x <= sum:
        break
    else:
        i += 1
print(i + 1)


