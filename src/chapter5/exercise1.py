try:
    #initialization
    count = 0
    total = 0
    average = 0

    # while loop to prompt the user and to do the iterations
    while True:
        user_input = input("Enter a number: ")

        if user_input == "done":
            break

        user_input = int(user_input)
        total += user_input
        count += 1
        average = total/count
    print(f"{total} {count} {average}")
except:
    print("Invalid Input")