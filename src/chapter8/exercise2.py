handle = open('mbox-short.txt')
count = 0
for line in handle:
    word = line.split()
    if len(word) == 0:
        continue
    if word[0] != 'From':
        continue
    print(word[2])