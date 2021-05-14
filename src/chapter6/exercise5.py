str = 'X-DSPAM-Confidence:0.8475'
word = str
word = float(word[word.index(":") + 1])
print(type(word))
