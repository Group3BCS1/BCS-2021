# this inputs the hours and rate
hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))

# this is a formulae for pay
pay = ((40 * rate) + ((hours - 40) * rate * 1.5))
print(float(pay))
