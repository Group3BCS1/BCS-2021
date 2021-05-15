handle = input('Enter the file name: ')
try:
    fhand = open(handle)
except:
    if handle == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        exit()
    else:
        print('File cannot be opened:', handle)
        exit()  # existing the program
count = 0

# reading through the file
for line in fhand:
    if line.startswith('Subject:'):
        count = count + 1
print('There were', count, 'subject lines in', handle)
