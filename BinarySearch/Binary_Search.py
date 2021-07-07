position = -1


def search(list, number):
    lower_bound = 0
    upper_bound = len(list)-1
    while lower_bound <= upper_bound:
        mid = (lower_bound+upper_bound)//2

        if list[mid] == number:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < number:
                lower_bound = mid
            else:
                upper_bound = mid


list = [4, 67, 5, 2, 8, 9, 53, 21]
list.sort()
number = int(input("Enter the number: "))

if search(list, number):
    print("Found at:  ",position+1)
else:
    print("Not found")
