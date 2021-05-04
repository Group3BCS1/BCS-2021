# main function
def water_bill():
    print("==========================RESTART==========================")
    code = input("Enter customer's code: ")
    code = code.lower()
    initial_reading = int(input("Enter beginning meter reading: "))
    final_reading = int(input("Enter Ending meter reading: "))

    def prompt_readings():
        """This function displays initial and final readings to the user"""
        print("Beginning Meter Reading: ", initial_reading)
        print("Ending Meter Reading: ", final_reading)

    def reading():
        """Function to Compute gallons of water used"""
        if initial_reading < final_reading:
            gallons = final_reading - initial_reading
            prompt_readings()
            gallons = gallons/10
            print("Gallons of water used ", gallons)
        else:
            if initial_reading > final_reading:
                gallons = 1000000000 - initial_reading
                gallons += final_reading
                gallons = gallons/10
                print("Gallons of water used ", gallons)
        return gallons



    reading()


water_bill()
