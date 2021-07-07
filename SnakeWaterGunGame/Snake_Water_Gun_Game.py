import random
import time
import string

possible_actions = ["Snake", "Water", "Gun"]
time.sleep(2)
print("------------------------------------------------\n")
print("Welcome to Rock , Paper & Scissors Game In Python\n")
print("--------------------------------------------------\n")
print("Rules:\nThere are two player one is you and other is computer\nWater will win from gun\nGun will win from snake\nSnake will win from water.")

time.sleep(1)
player_name = input("Enter your name: ")
time.sleep(1)
print("Computer have four player.Whom do you wanna play with?\n")
print("Player | Gender | Power | Level")
print("ALEX   | Male   | Blue  | I   ")
print("JOHN   | Male   | Green | II  ")
print("ROBERT | Male   | RED   | III ")
time.sleep(1)
print("\nSelect the player")
selected_player = input().capitalize()
if selected_player == "Alex" or "John" or "Robert":
    print(f"You have selected {selected_player}\n")
    time.sleep(1)
else:
    print("Kindly, select the above one of the player")
    selected_player = input("Enter the player again:")

print("---------------------------------------------")
print(f"{player_name} VS {selected_player}")
print("---------------------------------------------")
time.sleep(1)

while True:
    userInput = input("Enter your choice: ".capitalize())
    computer_action = random.choice(possible_actions)
    # ------------------User Selected Water-------------------
    if userInput == "Water":
        if computer_action == "Water":
            print("Both select Water,Game Tie")
        elif computer_action == "Gun":
            print(f"{player_name} Won!Water win from gun")
        elif computer_action == "Snake":
            print(f"{selected_player} Won!Snake win from water")
    # ------------------User Selected Paper-------------------
    elif userInput == "Gun":
        if computer_action == "Gun":
            print("Both select Gun,Game Tie")
        elif computer_action == "Snake":
            print(f"{player_name} Won! Gun win from snake")
        elif computer_action == "Water":
            print(f"{selected_player} Won! Water win from gun")
    # ------------------User Selected Scissors-------------------
    elif userInput == "Snake":
        if computer_action == "Snake":
            print("Both select Snake,Game Tie")
        elif computer_action == "Water":
            print(f"{player_name} Won! Snake win from water")
        elif computer_action == "Gun":
            print(f"{selected_player} Won! Gun win from snake")
    # Play Again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break

time.sleep(1)
print("\n\nThank you for playing")