import itertools


# main function
def water_bill():
    print("==========================RESTART==========================")
    code = input("Enter customer's code: ")
    code = code.lower()
    initial_reading = int(input("Enter beginning meter reading: "))
    final_reading = int(input("Enter Ending meter reading: "))
    print(" ")

    def prompt_readings():
        """This function displays initial and final readings to the user"""
        print(f"Beginning Meter Reading:  {initial_reading: 09}")
        print(f"Ending Meter Reading: {final_reading: 09}")

    def reading():
        """Function to Compute gallons of water used"""
        if initial_reading < final_reading:
            gallons = final_reading - initial_reading
            prompt_readings()
            gallons = gallons / 10
            print(f"Gallons of water used {gallons}")
        else:
            if initial_reading > final_reading:
                gallons = 1000000000 - initial_reading
                gallons = gallons + final_reading
                gallons = gallons / 10
                print(f"Gallons of water used {gallons}")
        return gallons

    def units():
        g = reading()
        four_million = 4000000
        ten_million = 10000000
        if code == "r":
            amount = 5.00 + (0.0005 * g)
            print(f"Amount billed: $ {round(amount, 2)}")
        else:
            if code == "c":
                if g <= four_million:
                    amount = 1000
                    print(f"Amount billed: $ {round(amount, 2)}")
                else:
                    if g > four_million:
                        addition_units = g - four_million
                        amount = 1000 + (0.00025 * addition_units)
                        print(f"Amount billed: $ {round(amount, 2)}")
            else:
                if code == "i":
                    if g <= four_million:
                        amount = 1000
                        print(f"Amount billed: $ {round(amount, 2)}")
                    else:
                        if four_million < g < ten_million:
                            amount = 2000
                            print(f"Amount billed: $ {round(amount, 2)}")
                        else:
                            if g > ten_million:
                                addition_units = g - ten_million
                                amount = 2000 + (addition_units * 0.00025)
                                print(f"Amount billed: $ {round(amount, 2)}")

    itertools.repeat(units(), 4)


water_bill()
