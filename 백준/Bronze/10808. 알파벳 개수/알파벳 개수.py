word = input()
alphabet = [0] * 26
for char in word:
    index = ord(char) - ord('a')
    alphabet[index] += 1
print(*alphabet)