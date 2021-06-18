fname = input('Enter the file name: ')
try:
  handle = open(fname)
except:
  print('File cannot be opened:', fname)
  exit()

emails = {}
for line in handle:
  lst = line.split()
  if len(lst) > 3 and line.startswith('From'):
    email = lst[1]
    # adding files to the dictionary
    if email not in emails:
      emails[email] = 1
    else:
      emails[email] += 1
print(emails)