from datetime import datetime


def validate_email():
    email = input("Enter your email:  ")
    if "@" in email and "gmail.com" in email:
        return(True , "Email is valid")
    return (False ,"Email is invalid")
print(validate_email())

def validate_number():
    number  = input("Enter your number with country code (e.g +92): ")
    if len(number) == 13 and "+" in number and number[1:].isdigit():
        return (True , "Number is valid")
    return (False, "Number is invalid")
print(validate_number())

def validate_date():
    date = input("Enter your registration date (e.g DD/MM/YYYY): ")
    current_date = datetime.now()
    try:
        parsed_date = datetime.strptime(date, "%d/%m/%Y")
        if parsed_date > current_date:
            return (False, "Date cannot be in the future")
        return (True, "Date is valid")
    except ValueError:
        return (False, "Invalid date format. Use DD/MM/YYYY")
print(validate_date())

def validate_password():
    password = input("Enter your password: ")
    if len(password) < 8:
        return (False , "Password contain at least 8 characters.")

    has_digit  = False
    for char in password:
        if char.isdigit():
            has_digit = True
    if not has_digit:
        return (False , "Password must be has one digit at least")      
    
    # Check 3: Special character
    if "@" not in password and "#" not in password and "&" not in password and "%" not in password:
        return (False, "Password must contain at least one special character")
    
    return (True, "Password is valid")
print(validate_password())

def validate_user_input():
    choice = input("What dou you want to validate(email/number/date/password):  ")
    if choice == "email":
        result = validate_email()
    elif choice == "number":
        result = validate_number()
    elif choice == "date":
        result = validate_date()
    elif choice == "password":
        result = validate_password()
    else:
        result = (False , "Invalid option")
    print(result)

validate_user_input()  

          
        
