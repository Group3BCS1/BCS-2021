prompt = input('Enter the File Name: ')
try:
	handle = open(prompt)
except:
	exit('Can\'t open the file')

address_dict = {}
for line in handle:
	lst = line.split()
	if len(lst) > 3 and line.startswith('From'):
		email_lst = lst[1].split('@')
		address = email_lst[1]

	#adding files to the dictionary
		if address not in address_dict:
			address_dict[address] = 1
		else:
			address_dict[address] += 1
print(address_dict)