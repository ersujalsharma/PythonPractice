# Guess the Number
a = 234  # this is the number

no_of_guess = 9  # Predeclared
while 1:
    print("Guess The Number")
    b = int(input())
    if no_of_guess == 0:
        print("Print Game Over")
        break
    else:
        if b == a:
            print("Nice Guess.")
            break
        elif b > a:
            print("Wrong Guess! You have entered wrong no:\n Your Number "
                  "is Greater than Guess Number")
            no_of_guess = no_of_guess - 1
            continue
        else:
            print("Wrong Guess! You have entered wrong no:\n Your Number "
                  "is Lesser than Guess Number")
            no_of_guess = no_of_guess - 1
            continue
