try:
    grade = int(input("Enter your grade out of 100: "))  # this will take user input and convert it to an integer

    if grade >= 90:                  # this will check if the grade is greater than or equal to 90
        print("You got an A+")       # this will print if the condition is true
    elif grade >= 80:                # this will check if the grade is greater than or equal to 80
        print("You got an A")        # this will print if the condition is true 
    elif grade >= 70:                # this will check if the grade is greater than or equal to 70
        print("You got a B")         # this will print if the condition is true
    elif grade >= 60:                # this will check if the grade is greater than or equal to 60
        print("You got a C")         # this will print if the condition is true
    elif grade >= 50:                # this will check if the grade is greater than or equal to 50
        print("You got a D")         # this will print if the condition is true
    else:
        print("Retry again!")            

except ValueError:  # this will catch the ValueError if the user enters a non-integer value
    print("Please enter a valid integer grade!")  # this will print if the ValueError is caught