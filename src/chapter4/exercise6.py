def compute_pay(hours, rate):
    """func to calculate the payment for the user when called"""
    try:
        hours = int(hours)
        rate = int(rate)

        if hours > 44:
            pay = ((40 * rate) + ((hours - 40) * rate * 1.5))
        else:
            pay = hours * rate
        print(float(pay))

    except:
        print("Error, Enter a numeric value")


# this is to input user data
compute_pay(input("Enter Hours: "), rate=input("Enter Rate: "))
