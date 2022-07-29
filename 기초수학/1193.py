"""분수찾기"""

x = int(input())
i, sum = 0, 0
while(1):
    sum += i
    if x <= sum:
        break
    i += 1

# 분자와 분모의 합 : i + 1
# 분자: a , 분모: b
if i % 2 == 0:
    a, b = i, 1
    # sum - x만큼 
    a = a - (sum - x) # a에는 빼주고
    b = b + (sum - x) # b에는 더해준다.
else:
    a, b = 1, i
    # sum - x만큼 
    a = a + (sum - x) # a에는 빼주고
    b = b - (sum - x) # b에는 더해준다.

print("%d/%d" % (a, b))
