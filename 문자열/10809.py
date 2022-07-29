"""알파벳 찾기"""

alphabet = [-1] * 26
word = list(input())

for i in range(len(word)):
    w = word[i]
    x = ord(w) - 97
    if alphabet[x] == -1:
        alphabet[x] = i

for i in alphabet:
    print(i, end=" ")