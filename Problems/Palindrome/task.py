word = input()
word_copy = list(word)
word_reversed = []
for _c in word:
    word_reversed.append(word_copy.pop())

if ''.join(word_reversed) == word:
    print("Palindrome")
else:
    print("Not palindrome")
