import random
import time
print("Load...")
time.sleep(1)
print("Load.......")
time.sleep(1)
print("Load..............")
time.sleep(1)
possible_actions = ["Rock", "Paper", "Scissors"]
time.sleep(1)
print("------------------------------------------------\n")
print("Welcome to Rock , Paper & Scissors Game In Python\n")
print("--------------------------------------------------\n")
print("Rules:\nThere are two player one is you and other is computer\nRock smashes scissors.\nPaper covers rock.\nScissors cut paper.\n")

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
if selected_player != "Alex" or "ALEX" or "alex" or "JOHN" or "john" or "John" or "ROBERT" or "Robert" or "robert":
    print("Kindly, select the above one of the player")
    selected_player = input("Enter the player again:").capitalize()
print(f"You have selected {selected_player}\n")
time.sleep(1)
print("---------------------------------------------")
print(f"{player_name} VS {selected_player}")
print("---------------------------------------------")
time.sleep(1)

while True:
    userInput = input("Enter your choice: ")
    computer_action = random.choice(possible_actions)
    # ------------------User Selected Rock-------------------
    if userInput == "Rock" or "rock" or "ROCK":
        if computer_action == "Rock":
            print("Both select Rock,Game Tie")
        elif computer_action == "Scissors":
            print(f"{player_name} Won!Rock smashes scissors")
        elif computer_action == "Paper":
            print(f"{selected_player} Won!Paper covers rock")
    # ------------------User Selected Paper-------------------
    elif userInput == "Paper" or "paper" or "PAPER":
        if computer_action == "Paper":
            print("Both select Paper,Game Tie")
        elif computer_action == "Rock":
            print(f"{player_name} Won!Paper covers rock")
        elif computer_action == "Scissors":
            print(f"{selected_player} Won! Scissors cut paper")
    # ------------------User Selected Scissors-------------------
    elif userInput == "Scissors" or "scissors" or "SCISSORS":
        if computer_action == "Scissors":
            print("Both select Scissors,Game Tie")
        elif computer_action == "Paper":
            print(f"{selected_player} Won!Paper covers rock")
        elif computer_action == "Rock":
            print(f"{selected_player} Won!Rock smashes scissors")
    # Play Again
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again != "yes":
        break

time.sleep(1)
print("Thank you for playing")