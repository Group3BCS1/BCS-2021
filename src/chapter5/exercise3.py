def vending():
    """This function contains a dictionary and a list to store th"""
    a = {"stock": "Nickels", "number": 25}
    b = {"stock": "Dimes", "number": 25}
    c = {"stock": "Quarters", "number": 25}
    d = {"stock": "Fives", "number": 0}
    e = {"stock": "Ones", "number": 0}

    stocks = [a, b, c, d, e]

    print("================================= RESTART =======================================")
    print("Welcome to our vending machine change maker program \nChange maker initialized.")


    def Display():
        """This function displays the stock to the user"""
        for stock in stocks:
            print(stock.get("number"), stock.get("stock"))


    def select_stock():
        """This function prompts the user to select stock and also quit
            This exits the program when "q" is entered
            if else its converts the input to float
        """
        select = input("Enter the purchase price (xx.xx) or `q' to quit: ")

        # This exception is to check for value errors
        try:
            if select == 'q':
                exit()
            else:
                select = float(select)
                return select
        except:
            print(f'Illegal price: Must be a non-negative multiple of 5 cents.')


    def select_deposit():
        """This function prompts the user for disposit"""

        select = input("Indicate your deposit: ")
        return select

    # initialize constants
    nickel_deposit = 0.05
    dimes = 0.1
    quarters = 0.25
    one_dollar = 1
    five_deposit = 5

    #initializing Display to the stock
    Display()

    while True:
        try:
            # a variable to hold the select function
            s = select_stock()





        except:
            print("Illegal price: Must be a non-negative multiple of 5 cents.")

if __name__ == '__main__':
    vending()
