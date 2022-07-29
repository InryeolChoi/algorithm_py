"""크로아티아 알파벳"""

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for c in croatia:
    word = word.replace(c, '*')
print(len(word))