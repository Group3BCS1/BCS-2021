fname = input('Enter the file name: ')
try:
  handle = open(fname)
except:
  print('Cant open file:', fname)
  exit()

days_dict = {}

for line in handle:
  days_list = line.split()
  if len(days_list) > 3 and line.startswith('From'):
    day = days_list[2]
    if day not in days_dict:
      days_dict[day] = 1
    else:
      days_dict[day] += 1
print (days_dict)