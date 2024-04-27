print("Welcome to Treasure island.\nYour mission is to find the treasure.")
direction=str(input("You're at a cross road. where do you want to go? Type \"left\" or \"right\"."))
if direction=="left":
    headforward=str(input("You've come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat or \"swim\" to swim across."))
    if headforward=="wait":
        door=str(input("You've arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. which color do  you choose?"))
        if door=="yellow":
            print("You've won")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")