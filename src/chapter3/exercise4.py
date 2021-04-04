try:

    age = int(input("How old are you: "))

    #if statement
    if age < 0:
        print("You are a time traveller")
    else:
        if 0 < age <= 17:
            print("Too young to vote")
        else:
            if age >= 18:
                print("You can vote")
except:
    print("Please use only numeric values")
