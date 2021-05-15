handle = open("mbox-short.txt")
for line in handle:
    line = line.strip()
    print(line.upper())