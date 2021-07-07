import time
import string
import random

def introduction():
    print("After a drunken night out with friends, you awaken the "
          "next morning in a thick, dank forest. Head spinning and "
          "fighting the urge to vomit, you stand and marvel at your new, "
          "unfamiliar setting. The peace quickly fades when you hear a "
          "grotesque sound emitting behind you. A slobbering orcis "
          "running towards you. You see all things are covered with blood walls.It's really dark and all you can see is three doors.They lead east, north and west. What do you do?In one of the direction there are 100 tigers\n\n")
    time.sleep(1)
    direction = input("Enter the direction you will move to? ").capitalize()
    print(direction)
    if direction == "East":
        East_direction()
    elif direction=="West":
        West_direction()    
    elif direction == "North":
        tiger_action()
    else:
        print(
            "You have only three dircetion.Select any one of them to survive or else die.")

def East_direction():
    print("\nYou have moved to east direction now there are three rooms\nSelect any direction\nKeep that in my mind that there is a witch in one of the direction\n")
    time.sleep(1)
    east_direction_option = input("Enter the direction: ").capitalize()
    print(east_direction_option)
    if east_direction_option=="East":
        West_direction()
    elif east_direction_option=="North":
        witch_action()
    elif east_direction_option=="West":
        North_direction()    
    else:
        print(f"You have eaten by a big spider because you haven't selected any direction.")    


def West_direction():
    print("\nYou have moved to West direction.Now there are three rooms\nSelect any direction\nKeep that in my mind that there is a witch in one direction and 100 of tigers in another direction.You have only one way to survive\n")
    time.sleep(1)
    west_direction_option=input("Enter the direction: ").capitalize()
    if west_direction_option=="East":
        witch_action()
    elif west_direction_option=="North":
        tiger_action()    
    elif west_direction_option=="West":
        depend_flower()
    else:
        print(f"You have eaten by a big spider because you haven't selected any direction.")

def North_direction():
    print("\nYou have moved to North direction.Now there are three rooms\nSelect any direction\nKeep that in my mind that there is a witch in one of the direction\n")
    time.sleep(1)
    north_direction_option=input("Enter the direction: ").capitalize()
    time.sleep(1)
    if north_direction_option=="East":
        witch_action()
    elif north_direction_option=="North":
        depend_flower()
    elif north_direction_option=="West":
        West_direction()        

def depend_flower():
    print("You have entered in a cave.There is a one flower over a big stone.We don't know wether it open the door of city heaven or it will destory the cave.\n")
    time.sleep(1)
    print("It is depend on your luck!")
    time.sleep(0.5)
    print("Believe on God! And try your luck")
    time.sleep(0.5)
    flower_luck=input("Enter pluck to see what happen: ").capitalize()
    if flower_luck =="Pluck":
        print("1")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("3")
        time.sleep(1)
        user_luck_action = random.choice(possible_actions)
        print(user_luck_action)
    else:
        time.sleep(1)
        print(f"You have entered{flower_luck}.....")
        time.sleep(1)
        print("It has opened all the door")
        time.sleep(1)
        print("Except of city heaven door")
        time.sleep(1)
        print("Tiger's & Witch: FINALLY !We have our lunch")
        time.sleep((0.5))
        print(f"{player_name}:hhhhhhhhhhh, DEAD.")
        time.sleep(1)
        print("Game Over......")

def tiger_action():
    print("Tigers were attending a party and unfortunately they were had not enough lunch.They had was you.\n")
    time.sleep(1)
    print("Tiger's:HURRYY!We have found a great lunchhad a great lunch by eating you")
    time.sleep((0.5))
    print(f"{player_name}:hhhhhhhhhhh, DEAD.")
    time.sleep(1)
    print("Game Over......")

def witch_action():
    print("Opps! Witch was you.")
    time.sleep(1)
    print("Witch: WOOWW HUMAN\nIts gonna a party tonight")
    print(f"{player_name}:hhhhhhhhhhh, DEAD.")
    time.sleep(1)
    print("Game Over......")    

if __name__ == "__main__":
    possible_actions = ["Congratulations! You have opened the door of city heaven.", "BAD LUCK. You have plucked the flowe on wrong time.\nCAVE DESTORED ."]
    print("Load...")
    time.sleep(1)
    print("Load.......")
    time.sleep(1)
    print("Load..............")
    time.sleep(1)
    print("------------------------------------------------\n")
    print("Welcome to Text-based Adventure Game In Python\n")
    print("--------------------------------------------------\n")
    time.sleep(1)
    player_name = input("Enter your name: ")
    introduction()