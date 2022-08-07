"""서로 다른 부분 문자열"""

data = input()
x = []
for i in range(len(data)):
    for j in range(i, len(data)):
        temp = data[i:j+1]
        x.append(temp)
print(len(set(x)))
