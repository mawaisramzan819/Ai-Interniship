first_number = float(input("Enter first number: "))     
second_number = float(input("Enter second number: "))

function = input("Enter the operation you want to perform (+, -, *, /): ")

if function == "+":
    result  = first_number + second_number

    print("The result of addition is:", result)

elif function == "-":
    result  = first_number - second_number

    print("The result of subtraction is:", result)

elif function == "*":
    result  = first_number * second_number

    print("The result of multiplication is:", result)


elif function == "/":
    if second_number == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result  = first_number / second_number
        print("The result of division is:", result)