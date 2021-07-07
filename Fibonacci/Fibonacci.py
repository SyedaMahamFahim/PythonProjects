def Fibonaaci_series(fibonaaci_range):
    first_value=0
    second_value=1
    third_vale=0
    for i in range (fibonaaci_range):
        first_value=second_value
        second_value=third_vale
        third_vale=first_value+second_value
        print(f"{third_vale} , ",end='')
        i=int(i+1)

if __name__ == "__main__":
    print("Fibonaaci Series")
    fibonaaci=int(input("Enter the range of Fibonaaci Series: "))
    print(f"The Fibonaaci Series is: ")
    Fibonaaci_series(fibonaaci)