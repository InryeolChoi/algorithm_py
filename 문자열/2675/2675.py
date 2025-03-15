"""문자열 반복"""

for _ in range(int(input())):
    n, word = input().rstrip().split(" ")
    for x in list(word):
        for i in range(int(n)):
            print(x, end="")
        print("", end="")
    print("")