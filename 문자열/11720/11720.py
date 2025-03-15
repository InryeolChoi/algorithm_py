"""숫자의 합"""
x = int(input())
num = list(input())
sum = 0
for i in range(x):
    sum += int(num[i])
print(sum)
