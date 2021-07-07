import random
import time
print("---------------------------------------------\n")
print("Welcome to Guess The Number Game In Python\n")
print("---------------------------------------------\n")
print("Rules:\nThere are two player one is you and other is computer\n1-You have 5 lives\nYou have to guess in between 10 to 100\nIf whoever guessed the number in less live , will be the winner\n\n")
time.sleep(1)
player_name = input("Enter your name: ")
time.sleep(1)
print("Computer have four player.Whom do you wanna play with?")
print("Player | Gender | Power | Level")
print("ALEX   | Male   | Blue  | I   ")
print("JOHN   | Male   | Green | II  ")
print("ROBERT | Male   | RED   | III ")
print("BELLA  | FeMale | Black | IV  ")
time.sleep(1)
print("Select the player")
selected_player = input()
print(f"You have selected {selected_player}\n")
time.sleep(1)
print("---------------------------------------------")
print(f"{player_name} VS {selected_player}")
print("---------------------------------------------")

random_number = int(random.randint(10, 100))
print(random_number)
player_lives = 1
lives_count = int(4)
time.sleep(1)
print("---------------------------------------------")
print(f"{player_name} Turn")
print("---------------------------------------------")
print(f"Player {player_name} have 5 lives")
while(player_lives <= 5):
    player_guess = int(input("Enter the guess number: "))
    if player_guess == random_number:
        print(
            f"Excellent! You have guessed correctly.\nYou have guess this in {player_lives}\n")
        break
    elif player_guess > random_number:
        print("Too High! Try again")
        print(f"{player_name} have {lives_count} lives left\n")
    elif player_guess < random_number:
        print("Too low! Try again")
        print(f"{player_name} have {lives_count} lives left\n")
    player_lives = int(player_lives+1)
    lives_count = int(lives_count-1)


time.sleep(1)
print("---------------------------------------------\n")
print(f"{selected_player} Turn")
print("---------------------------------------------\n")
computer_lives = 1
computer_count_lives = int(5)
print(f" Player {selected_player} have 5 lives")
time.sleep(1)
while (computer_lives <= 5):
    computer_random_number = int(random.randint(10, 100))
    time.sleep(1)
    print(f"{selected_player} has guess: {computer_random_number}")
    if computer_random_number == random_number:
        print(
            f"Excellent! {selected_player} have guessed correctly.\n{selected_player} have guessed this in {computer_lives}")
        break
    elif computer_random_number > random_number:
        print("Too High! Try again\n")
        print(f"{selected_player} have  lives {computer_count_lives} left")
    elif computer_random_number < random_number:
        print("Too low! Try again\n")
        print(f"{selected_player} have  lives {computer_count_lives} left")
    computer_lives = int(computer_lives+1)
    computer_count_lives = int(computer_count_lives-1)

time.sleep(2)
print("---------------------------------------------\n")
print("Game Result")
print("---------------------------------------------\n")
if player_lives < computer_lives :
    print(f"{player_name} had guessed the number in {player_lives} lives  ")
    print(f"{player_name} is winner")
elif player_lives < computer_lives :
    print(f"{selected_player} had guessed the number in {selected_player} lives")
    print(f"{selected_player} is winner") 
else:
    print("Game Over! No one is winner")     
