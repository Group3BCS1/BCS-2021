handle = open("mbox.txt")
for line in handle:
    line = line.strip()
    print(line.upper())