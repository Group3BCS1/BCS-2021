c = int(input("Enter initial amount of investment: "))
r = float(input("Enter the rate(eg 0.02 is 20%): "))
t = int(input("Enter number of years until maturation: "))
n = int(input("Enter the number of times the interest is compounded per year: "))

p = (c*(1 + (r/n))**(t*n))

print(f"The final value of investment: {round(p, 2)}")
