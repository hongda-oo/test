# Ask for player's name
name = input("Type your name: ")
print("Welcome", name, "to the adventure!")

print("You wake up in a dark forest. You see a path to the LEFT and a river to the RIGHT.")

# Input validation: player must choose LEFT or RIGHT
choice1 = input("Do you go LEFT or RIGHT? ").lower()
while choice1 not in ["left", "right"]:
    choice1 = input("Please type LEFT or RIGHT: ").lower()

# LEFT PATH 
if choice1 == "left":
    print("You walk along the path and find an old house.")

    # Input validation: KNOCK or WALK 
    choice2 = input("Do you KNOCK on the door or WALK away? ").lower()
    while choice2 not in ["knock", "walk"]:
        choice2 = input("Please type KNOCK or WALK: ").lower()

    # Player chooses to knock
    if choice2 == "knock":
        print("An old wizard opens the door and smiles.")

        #  Input validation: TREASURE or SECRET 
        choice3 = input("He offers you a TREASURE or SECRET. Which do you choose? ").lower()
        while choice3 not in ["treasure", "secret"]:
            choice3 = input("Please type TREASURE or SECRET: ").lower()

        # Treasure ending
        if choice3 == "treasure":
            print("You receive a chest of gold. You win!")

        # Secret ending
        else:  # secret
            print("He tells you the meaning of life. You feel at peace. You win in a different way.")

    # Player chooses to walk away
    else:  # walk
        print("You walk away, but get lost in the forest. Game over.")

#  RIGHT PATH 
elif choice1 == "right":
    print("You walk to the river and see a small BOAT and a BRIDGE.")

    # Input validation: BOAT or BRIDGE
    choice2 = input("Do you take the BOAT or cross the BRIDGE? ").lower()
    while choice2 not in ["boat", "bridge"]:
        choice2 = input("Please type BOAT or BRIDGE: ").lower()

    # Player chooses the boat
    if choice2 == "boat":
        print("You row into the fog and reach a hidden island.")

        # Input validation: EXPLORE or PICK 
        choice3 = input("On the island, do you EXPLORE the cave or PICK fruit from the trees? ").lower()
        while choice3 not in ["explore", "pick"]:
            choice3 = input("Please type EXPLORE or PICK: ").lower()

        # Explore ending
        if choice3 == "explore":
            print("You find ancient ruins and become a famous explorer. You win!")

        # Pick fruit ending
        else:  # pick
            print("The fruit was poisonous... Game over.")

    # Player chooses the bridge
    else:  # bridge
        print("The bridge breaks and you fall into the river. Game over.")