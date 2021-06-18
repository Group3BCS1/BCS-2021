import string
handle = open('words.txt', 'r')
words = {}
lst = []

for line in handle:
    line = line.translate(line.maketrans('', '', string.punctuation))
    word_lst = line.split()
    lst += word_lst
    for word in word_lst:
        if word in word_lst:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1

print(words)
while True:
    check = input('Which string would u like to check for: ')
    if check in words:
        print("Yes it exists!")
    else:
        print('No its does not exist')