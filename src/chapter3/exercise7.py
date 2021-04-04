try:
    location = input("enter location: ")
    location = location.upper()  # this converts the user's string to uppercase

    pay = float(input('enter pay: '))
    if location == 'MBARARA' and pay > 4000000:
        print('I WILL TAKE THE JOB')
    elif location == 'MBARARA' and pay <= 4000000:
        print('SORRY, I CAN NOT WORK FOR THAT')
    elif location == 'KAMPALA' and pay > 10000000:
        print('I WILL DEFINITELY WORK')
    elif location == 'KAMPALA' and pay <= 10000000:
        print('NO WAY !')
    elif location == 'SPACE' and pay >= 0:
        print('WITHOUT DOUBT, I WILL TAKE IT')
    elif pay >= 6000000:  # x==other districts and y>=6000000
        print('I will surely work')
    else:
        print('No thanks, I can find something better')
except:
    print('invalid entry') # this is printed when the user enters an invalid input
