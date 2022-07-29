"""단어 공부"""

alphabet = [0] * 26
word = list(input().lower())
for w in word:
    alphabet[ord(w)-97] += 1

x = []
for i in range(26):
    if alphabet[i] == max(alphabet):
        x.append(chr(i + 65))
if len(x) > 1:
    print("?")
else:
    print(x[0])

