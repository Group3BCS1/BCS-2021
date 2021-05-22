handle = open("../chapter8/mbox-short.txt")
for line in handle:
    line = line.strip()
    print(line.upper())