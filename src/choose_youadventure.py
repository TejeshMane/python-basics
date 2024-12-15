print("Welcom to adventure game")
name = input("What is your name: ").capitalize()
print(f"Hello {name} lets start the game")

answer = input(
    "You are in middle of trekking and you find 2 routes, left and right which one will you choose(left/right) ? "
).lower()

if answer == "right":
    answer = input(
        "After taken right there is river do you want to swin or walk accross (swim/walk) "
    ).lower()
    if answer == "walk":
        print("you walk and ran out of water you loose")
    elif answer == "swim":
        print("you swim and eaten by crocs")
    else:
        print("This is not a valid option you loose")

elif answer == "left":
    answer = input(
        "After taken Left there is mountain do you want to trek or walk accross (trek/walk) "
    ).lower()
    if answer == "trek":
        answer = input(
            "you trek and reach mountain top you see on door will you open or let it go: (open/ignore) "
        ).lower()
        if answer == "open":
            print("you open and find loot kept by pirtaes on mountain top you WIN!!!.")
        elif answer == "ignore":
            print("yyou ignore and lost opportunity to got gold inside the door")
        else:
            print("This is not a valid option you loose")
    elif answer == "walk":
        print("you walk and lost in jungle you loose")
    else:
        print("This is not a valid option you loose")
else:
    print("This is not a valid option you loose")
