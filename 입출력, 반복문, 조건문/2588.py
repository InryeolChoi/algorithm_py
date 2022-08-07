"""곱셈"""

input1 = int(input())
input2 = input()

for i in reversed(range(3)):
    print(input1 * int(input2[i]))
print(input1 * int(input2))