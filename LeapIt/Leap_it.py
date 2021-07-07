
def leapYear(year_enter):
    if year_enter %4==0 or year_enter % 400==0:
        print(f"{year_enter} is a leap year")
    elif year_enter %100==0:
        print("It is not a leap year")   
    else:
        print("Hello world")     

if __name__ == "__main__":
    print("Leap Year")
    year=int(input("Enter any year to find out whether it is Leap year or not: "))
    leapYear(year)
    