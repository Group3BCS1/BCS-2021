try:
    # inputs the score from the user
    score = float(input("Enter Score: "))

    # the is the if else statement to  determine the grade

    if 0.9 <= score <= 1.0:
        print("A")

    # this is when the if statement is not true
    else:
        if 0.8 <= score < 0.9:
            print("B")
        else:
            if 0.7 <= score < 0.8:
                print("C")
            else:
                if 0.6 <= score < 0.7:
                    print("D")
                else:
                    if 0.0 <= score < 0.6:
                        print("F")
                    else:
                        if score > 1.0:
                            print("Bad Score")
except:
    print("Bad Score")
