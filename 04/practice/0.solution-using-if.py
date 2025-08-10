import random

welcome_message = """
------------------------
Rock Paper Scissors Game
------------------------
You can play with:
1.Rock
2.Paper
3.Scissors
------------------------"""

print(welcome_message)

game_chicess = ["rock", "paper", "scissor"]

while 1:
    computer_choice = random.choice(game_chicess)
    print("C:", computer_choice)

    user_pick = input("> what do you pick:")
    user_pick = user_pick.lower()
    print("U:", user_pick)

    if user_pick not in game_chicess:
        print("invalid input try again")

    if user_pick == "rock" and computer_choice == "rock":
        print("i choosed "+computer_choice+" tie :|")

    if user_pick == "paper" and computer_choice == "paper":
        print("i choosed "+computer_choice+" tie :|")

    if user_pick == "scissor" and computer_choice == "scissor":
        print("i choosed "+computer_choice+" tie :|")

    #######################

    if user_pick == "scissor" and computer_choice == "paper":
        print("i choosed "+computer_choice+" win :)")

    if user_pick == "paper" and computer_choice == "rock":
        print("i choosed "+computer_choice+" win :)")

    if user_pick == "rock" and computer_choice == "scissor":
        print("i choosed "+computer_choice+" win :)")

    #######################

    if computer_choice == "scissor" and user_pick == "paper":
        print("i choosed "+computer_choice+" lose :(")

    if computer_choice == "paper" and user_pick == "rock":
        print("i choosed "+computer_choice+" lose :(")

    if computer_choice == "rock" and user_pick == "scissor":
        print("i choosed "+computer_choice+" lose :(")