# vending machine change maker programme.
# function that has menu for selection of bill/money to be deposited
def selection_menu():
    print("Menu for deposits")
    print("'n'- deposit a nickel\n'd' - deposit a dime\n'q' - deposit a quarter\n"
          "'o' - deposit a one dollar bill\n'f' - deposit a five dollar bill"
          "\n'c' - cancel the purchase")


# main programme starts off here
print("Welcome to the vending machine change maker programme")
print("Change maker initialized")
print("Stock contains:")
n = 25
d = 25
q = 25
o = 0
f = 0
print(f"{n} nickels\n{d} dimes\n{q} quarters\n{o} ones\n{f} fives")
# requesting for price from the user
while True:
    try:
        # requesting for price input
        price = input("Enter the purchase price (xx.xx) or `q' to quit:")
        if price == "q":
            break
        item_cost = float(price)
        if (item_cost > 0) and round((item_cost * 100) % 5 == 0):
            selection_menu()
        else:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")
    except:
        print("Input can't be rendered, please enter a non-negative multiple of 5 cents ")