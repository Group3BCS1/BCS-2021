# This program computes compound interest

def investment(c, r, n, t):
    try:
        # converting variable data
        c = int(c)
        r = float(r)
        n = int(n)
        t = int(n)

        # investment formulae
        p = c * (1 + (r / n) ** t * n)

        # rounding off the result and outputting the result
        print(f"Your final value for investment is {round(p, 2)}")
        return p
    except:
        print("\n \nEnter valid inputs(numerical values)")


investment(c=input('Enter the initial amount of an investment(C): '),
           r=input('Enter the yearly rate of interest(r): '),
           n=input('Enter the number of years until maturation(t): '),
           t=input('Enter the number of times the interest is compounded per year(n): '))
