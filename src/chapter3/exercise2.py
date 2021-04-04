try:
    hours = int(input("Enter Hours: "))
    rate = int(input("Enter Rate: "))

    pay = ((40 * rate) + ((hours - 40) * rate * 1.5))
    print(float(pay))
except:
    print("Error, Enter a numeric value")
