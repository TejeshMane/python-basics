import random

top_of_range = input("type a number for top of range?")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range < 0:
        print("enter number greater than 0")
        quit()
else:
    print("Enter number next time")
    quit()


# game_on = input("would you like to play game?")
# print(game_on)

# if game_on.lower() == "yes":
#     print("started the game")
#     number_range = input("select the range of number?")
#     random_num = random.randint(0, int(number_range))
#     print(random_num)

# else:
#     print("game will not start")


# num = random.randint(0, 10)
# print(num)
