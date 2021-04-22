try:
    num_lst = []

    while True:
        user_input = input("Enter a Number: ")

        if user_input == "done":
            break
        user_input = int(user_input)
        num_lst.append(user_input)
        maximum = max(num_lst)
        minimum = min(num_lst)

    print(f"Smallest Number is {minimum}\nLargest Number is {maximum}")
except:
    print("invalid input")
    