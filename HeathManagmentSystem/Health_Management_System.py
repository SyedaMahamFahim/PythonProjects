import string
import datetime


def getdate():
    return datetime.datetime.now()


def food_log_of_members(name_of_members):

    if name_of_members == "Maham":
        f = open("mahamfood.txt")
        print(f.read()+"\n")
        f.close()
    elif name_of_members == "Ayesha":
        f = open("ayeshafood.txt")
        print(f.read()+"\n")
        f.close()
    elif name_of_members == "Rahima":
        f = open("rahimafood.txt")
        print(f.read()+"\n")
        f.close()
    else:
        print("Kindly,Enter the name of any of above gym member")


def food_retrieve_of_members(name_of_members):

    if name_of_members == "Maham":
        f = open("mahamfood.txt", "r+")
        print(f.read()+"\n")
        print("Continue from here: ")
        f.write(input("\n")+"\n")
        f.close()
        print("\nSuccessfully written")
    elif name_of_members == "Ayesha":
        f = open("ayeshafood.txt", "r+")
        print(f.read()+"\n")
        print("Continue from here: ")
        f.write(input("\n")+"\n")
        f.close()
        print("\nSuccessfully written")
    elif name_of_members == "Rahima":
        f = open("rahimafood.txt", "r+")
        print(f.read()+"\n")
        print("Continue from here: ")
        f.write(input("\n")+"\n")
        f.close()
        print("\nSuccessfully written")
    else:
        print("Kindly,Enter the name of any of above gym member")


def exercise_log_of_members(name_of_members):
    if name_of_members == "Maham":
        f = open("mahamexercise.txt")
        print(f.read())
        f.close()
    elif name_of_members == "Ayesha":
        f = open("ayeshaexercise.txt")
        print(f.read())
        f.close()
    elif name_of_members == "Rahima":
        f = open("rahimaexercise.txt")
        print(f.read())
        f.close()
    else:
        print("Kindly,Enter the name of any of above gym member")


def exercise_retrieve_of_members(name_of_members):

    if name_of_members == "Maham":
        f = open("mahamexercise.txt", "r+")
        print(f.read())
        print("Continue from here: ")
        f.write(input("")+"\n")
        f.close()
        print("\nSuccessfully written")
    elif name_of_members == "Ayesha":
        f = open("ayeshaexercise.txt", "r+")
        print(f.read())
        print("Continue from here: ")
        f.write(input("")+"\n")
        f.close()
        print("\nSuccessfully written")
    elif name_of_members == "Rahima":
        f = open("rahimaexercise.txt", "r+")
        print(f.read())
        print("Continue from here: ")
        f.write(input("")+"\n")
        f.close()
        print("\nSuccessfully written")
    else:
        print("Kindly,Enter the name of any of above gym member")


print("\n\n \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\Health Management System\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n\n")
date_time = getdate()
list_of_members = ["Maham", "Ayesha", "Rahima"]
print("There are three members in gym\n1-Maham \3\n2-Ayesha \3\n3-Rahima \3")
print("\nYou can log their information or edit their information\n")
choice = input(
    "Enter Log for see their information or Enter Retrieve to edit their information\n").capitalize()
selected_name = input("Enter the name of member: ").capitalize()


if choice == "Log":

    if selected_name in list_of_members:
        selected_log = input(
            f"You have selected {selected_name}.What do you want to see ?\nFood Log\nExercise Log: ")
        if selected_log == "Food Log" or "food log":
            print(f"\n[{date_time}]\n")
            food_log_of_members(selected_name)
            print("\n")

        elif selected_log == "Exercise Log" or "exercise log":
            print(f"\n[{date_time}]\n")
            exercise_log_of_members(selected_name)
            print("\n")
        else:
            print("Kindly, select Food log or Exercise log")
    else:
        print("Kindly,Enter the name of any of above gym member")

elif choice == "Retrieve":
    if selected_name in list_of_members:
        selected_retrieve = input(
            f"You have selected {selected_name}.What do you want to edit ?\nFood Retrieve\nExercise Retrieve: ")
        if selected_retrieve == "Food Retrieve" or "food retrieve" :
            print(f"\n[{date_time}]\n")
            food_retrieve_of_members(selected_name)
            print("\n")

        elif selected_retrieve == "Exercise Retrieve" or "exercise retrieve":
            print(f"\n[{date_time}]\n")
            exercise_retrieve_of_members(selected_name)
            print("\n")
        else:
            print("Kindly, select Food Retrieve or Exercise Retrieve")
    else:
        print("Kindly,Enter the name of any of above gym member")
else:
    print("Kindly,Enter the Retrieve or Log ")