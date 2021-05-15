prompt = input('Enter the file name: ')
try:
    prompt = open(prompt)
except:
    print('File cannot be opened:', prompt)
    exit()
total = 0
count = 0
# reading through the file
for line in prompt:
    if line.startswith("X-DSPAM-Confidence:"):
        # removes lines after and before a sentence
        line = line.strip()
        pos = line.index(":")
        f_num = float(line[pos + 1:])

        count += 1
        total = total + f_num
        average = total/count

print(f'Average Spam Confidence {average}')
