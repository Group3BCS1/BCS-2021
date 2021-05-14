prompt = open(input("Enter the file name: "), 'r')
total = 0
count = 0
for line in prompt:
    if line.startswith("X-DSPAM-Confidence:"):
        line = line.strip()
        pos = line.index(":")
        f_num = float(line[pos + 1:])

        count += 1
        total = total + f_num
        average = total/count

print(f'Average Spam Confidence {average}')
