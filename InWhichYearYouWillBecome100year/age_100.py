"""
Take age or year of birth as an input from the user. Store the input in one variable. Your program should detect whether the entered input is age or year of birth and tell the user when they will turn 100 years old. (5 points).

Here are a few instructions that you must have to follow:

Do not use any type of modules like DateTime or date utils. (-5 points)
Users can optionally provide a year, and your program must tell their age in that particular year. (3points)
Your code should handle all sort of errors like:                       (2 points)
You are not yet born
You seem to be the oldest person alive
You can also handle any other errors, if possible!

"""
"""
age_or_year = input("Enter your age or date of birth: ")
alpha=age_or_year.isalpha()
if int(age_or_year) < 1 or int(age_or_year) > 2021 or len(age_or_year) == 5:
    print("You are not born yet")
elif len(age_or_year) == 2 or len(age_or_year) == 3 or len(age_or_year) == 1:
    cal = int(2021+100)-(int(age_or_year))
    print(f"You will be 100 years old in  {cal}")
elif len(age_or_year) == 4:
    cal = 100+int(age_or_year)
    print(f"You will be 100 years old in  {cal}")
elif alpha==True:
    print("Kindly Enter the correct age or date of birth")    
"""

while True:
    age_or_year = input("Enter your age or date of birth: ")
    if (age_or_year.isalpha())==False:
        if int(age_or_year) < 1 or int(age_or_year) > 2021 or len(age_or_year) == 5:
            print("You are not born yet")    
        elif len(age_or_year) == 2 or len(age_or_year) == 3 or len(age_or_year) == 1:
            cal = int(2021+100)-(int(age_or_year))
            print(f"You will be 100 years old in  {cal}")
        elif len(age_or_year) == 4:
            cal = 100+int(age_or_year)
            print(f"You will be 100 years old in  {cal}")
        break
    elif (age_or_year.isalpha())==True:
        print("Kindly Enter the correct age or date of birth")
        continue
    