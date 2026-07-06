def advanced_login():
    try:
    
        user_name = input("Enter Your username: ")  # user enter his username 
        if not user_name:                           # not opertor used for username cannot blank.
            return ("Username cann't be blank")
        elif len(user_name) > 6:                     #  this is define lenght of  username.
            return ("Username have at least 6 characters.")
        
        password = input("Enter password: ")           
        if len(password) < 8 or len(password) > 20 :         # this is define minimum or maximum length of password. 
         return ("Passeord must have 8 to 20 characters.")
        
        confirm_password = input("Confirm passeord: ")
        if password != confirm_password:                      # confirm the password
            return ("Password is not same try again!")
        
        age = int(input("Enter your age: "))
        if age >= 18:                                         #  age limit
            return ("Login successfull.")
        else:
            return ("Please fill the form according to term and conditions.")

    except ValueError:
        return("Enter valid input!")       # In the form of invalid input riase valueError message!
 

print(advanced_login())
