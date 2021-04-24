# Group 3 members
# ATWANZIRE TIMOTHY IAN 2020/BCS/026/PS
# AHWERA ATENSA 2020/BCS/014/PS
# OKELLO JOSHUA 2020/BCS/006
# MULIZA TYRONE 2020/BCS/074/PS

# main function
def vending():
    """This function contains a dictionary and a list to store the stock"""
    a = {"stock": "Nickels", "number": 25}
    b = {"stock": "Dimes", "number": 25}
    c = {"stock": "Quarters", "number": 25}
    d = {"stock": "Fives", "number": 0}
    e = {"stock": "Ones", "number": 0}

    stocks = [a, b, c, d, e]

    print("================================= START =======================================")
    print("Welcome to our vending machine change maker program \nChange maker initialized.")

    # Display Function
    def Display():
        """This function displays the stock to the user"""
        # For loop
        for stock in stocks:
            print(stock.get("number"), stock.get("stock"))

    # initialize constants
    n = 0.05
    d = 0.1
    q = 0.25
    o = 1
    f = 5

    def menu():
        print("""
        Deposit Menu
        'n' - deposit a nickel
        'd' - deposit a dime"
        'q' - deposit a quarter
        'o' - deposit a one dolla bill
        'f' - deposit a five dolla bill
        'c' - cancel the purchase
        """)

    def convert_entry(px):
        dolls = px // 1
        cents = (px % 1)
        print(f"Payment due: {dolls: .0f} dollars and {cents * 100:.0f} cents")

    Display()
    # main while loop

    while True:
        try:
            # prompting the user for price
            price_entry = input("Enter the purchase price (xx.xx) or `q' to quit: ")
            if price_entry == "q":
                print("Quiting...")
                break
            price_entry = float(price_entry)
            price = price_entry

            # if statement to check the price entry
            if (price > 0) and (((price * 100) % 5) == 0):
                menu()
                convert_entry(price_entry)
                dep_sum = 0.00

                while price > dep_sum:
                    deposit = input("Indicate your deposit: ")
                    if deposit == 'c':
                        print("Please take the change below", dep_sum)

                        break
                    elif deposit == 'n':
                        price -= n
                        dep_sum += 0.05
                        a["number"] = a["number"] + 1
                        convert_entry(price)
                        continue
                    elif deposit == 'd':
                        price = price - d
                        dep_sum = dep_sum + 0.1
                        b["number"] = b["number"] + 1
                        convert_entry(price)
                        continue
                    elif deposit == 'q':
                        price = price - q
                        dep_sum = dep_sum + 0.25
                        c["number"] = c["number"] + 1
                        convert_entry(price)
                        continue
                    elif deposit == 'o':
                        price = price - o
                        dep_sum = dep_sum + 1
                        d["number"] = c["number"] + 1
                        convert_entry(price)
                        continue
                    elif deposit == 'f':
                        price = price - f
                        dep_sum = dep_sum + 5
                        e["number"] = ["number"] + 1
                        convert_entry(price)
                        continue
                    else:
                        print("Illegal selection:", deposit)
                        convert_entry(price_entry)
                        continue
                if dep_sum == price:
                    print("No change!")

            else:
                print("Illegal price: Must be a non-negative multiple of 5 cents.")
        except:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")


vending()
