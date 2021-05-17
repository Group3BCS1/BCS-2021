try:
    handle = open("measles.txt", 'r')  # opening the file
except:
    exit()

f_name = input("Enter file name: ")
new_file = open(f_name, 'w')
year = input("Enter Year: ")
for line in handle:
    # comparing the year inputs
    if (year == line[88:92]) or (year == line[88:91]) or (year == line[88:90] or (year == line[88:89])):
        new_file.write(line)  # writing data in the new
    else:
        if (year == 'all') or (year == 'ALL') or (year == ' '):
            new_file.write(line)  # writing data in the new
