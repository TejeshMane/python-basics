import random

user_won = 0
computer_won = 0
ties = 0
options = ["rock", "paper", "scissor"]

while True:
    user_input = input("Enter you pick rock/paper/scissor or q to quit game: ").lower()
    if user_input == "q":
        break
    if user_input not in options:
        continue
    random_num = random.randint(0, 2)
    computer_pick = options[random_num]
    print(f"computer chosses : {computer_pick}.")

    if user_input == computer_pick:
        print("it is a tie")
        ties += 1
    elif user_input == "rock" and computer_pick == "scissor":
        print("You won!")
        user_won += 1
    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_won += 1
    elif user_input == "scissor" and computer_pick == "paper":
        print("You won!")
        user_won += 1
    else:
        print("Computer Won! You Loss")
        computer_won += 1
print(f"User won {user_won} times")
print(f"Computer won {computer_won} times")
print(f"Match ties {ties} times")
print("Goodby")
