def open_file():
    prompt = input("Enter Input File Name: ")
    try:
        f_name = open(prompt, 'r')
    except:
        print("Enter Valid File Name!")
        prompt = input("Enter Input File Name: ")
        f_name = open(prompt, 'r')
    return f_name


def process_file(open_file):
    low_income = 'WB_LI '
    lower_middle = 'WB_LMI'
    upper_middle = 'WB_UMI'
    high_income = 'WB_HI '
    year = input("Enter Year: ")
    level = """
    1 - Low income
    2 - Lower middle income
    3 - upper middle income
    4 - high income
    Enter income Level: 
    """
    income_level = input(level)
    count = 0
    total = 0
    for line in open_file:
        # comparing the year inputs
        if year == line[88:92]:
            if income_level == '1':
                if line[51:57] == low_income:
                    pos = line[58:61]
                    percent = float(pos)
                    count += 1
                    total += percent
                    print(line.strip())
                    continue
            elif income_level == '2':
                if line[51:57] == lower_middle:
                    pos = line[58:61]
                    percent = float(pos)
                    total += percent
                    count += 1
                    print(line.strip())
                    continue
            elif income_level == '3':
                if line[51:57] == upper_middle:
                    pos = line[58:61]
                    percent = float(pos)
                    count += 1
                    total += percent
                    print(line.strip())
                    continue
            elif income_level == '4':
                if line[51:57] == high_income:
                    pos = line[58:61]
                    percent = float(pos)
                    count += 1
                    total += percent
                    print(line.strip())
                    continue

    print(f'The total is {total}')
    print(f'The average is {total / count}')


open_file = open_file()
process_file(open_file)
