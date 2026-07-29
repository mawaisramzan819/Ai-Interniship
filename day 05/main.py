# Simple decision tree simulator
# User fill these things
age = int(input("Enter your age: "))
income = int(input("Enter your monthly Income: "))
credit_score = int(input("Enter your credit score: "))
# using error handly if user enters wrong or invalid input except of raisng error this show error message
try: 
    # using condtional statments for better understanding for user
    if age < 18:
        print("You are not eligible!")
    elif income < 30000:
        print("You are not eligible!")
    elif credit_score < 600 :
        print("You are not eligible!")
    else:
        print("Approved") 
 # this message will shown on the screen if user enter invalid input       
except ValueError:
    print("Invalid choice! Fill the form according to term and conditions.")                   




