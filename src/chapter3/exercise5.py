try:
    no = int(input("How many people are attending the wedding: "))
    if no <= 50:
        print("It will cost you $4,000")
    elif no <= 100:
        print("It will cost $10,000")
    elif no <= 200:
        print("It will cost $15,000")
    else:
        print("It will cost $20,000")
except:
    print("Please enter a numeric value")
