import random
import time
import string

def dice_roll():
    while True:
        roll = input("Enter roll to roll the dice: ").capitalize()
        if roll == "Roll":
            random_number = int(random.randint(1, 7))
            print(f"The dice roll to : {random_number}")
        else:
            print("Kindly enter roll to roll the dice")

        play_again = input(
            "Do you want to play again? if yes then type yes or no: ").capitalize()
        if play_again == "Yes":
            continue
        else:
            break

if __name__ == "__main__":
    print("------------------------------------------------\n")
    print("Welcome to Dice Rolling Simulator Game In Python\n")
    print("------------------------------------------------\n")
    player_name = input("Enter your name: ")
    time.sleep(1)
    dice_roll()
    print("Thank you for playing")