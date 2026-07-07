def multioperator_calculator():   # define a function in which actions perform

    try:               # set error handling 

        num1 = float(input("Enter number 1: "))          # user enters number1 to perform action
        num2 = float(input("Enter number 2: "))          # user enters number2 to perform action
        operator = input("Enter operation to perform (+,-,*,/):  ").strip()     #  user select action to perform
        # using conditional statment for perform operations
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2 
        elif operator == "*":
            return num1 * num2 
        elif operator == "/":
            if num2 == 0:
                return ("Division by zero is not allowed!")
 
        # if user enters invalid input except of raising error it can handle by valueError
    except ValueError:

        return ("Invalid input! Please enter numeric values.")

print(multioperator_calculator())    # display output on screen    
 

        
