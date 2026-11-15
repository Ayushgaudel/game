do_continue="y"

def haunted():
    print("Welcome🙏,\nYou are in a haunted place")
    print( "A Girl is crying just behind you😱")
    player1 = input("Turn behind: Y/N:").lower().strip()
    if player1 == "y":
        print("WOWW!!, You are safe😅\n It was just a radio")
        print("You also got some coins🪙")
        playerinput2 = input("Lets move and explore this place (y or n):").lower().strip()
        print(playerinput2)
        if playerinput2 == "y":
            playerinput4 = input("There's soemthing near the tree \n Go check(G) or run away(R):").lower().strip()

            if playerinput4 == "g":
                print("ohh!! Thats a cat, \n you are safe")
                user_input0 = input("Now enjoy the view of the game \n The game ends......")
            elif playerinput4 == "r":
                print("You must run fast something is chasing you")
                print("Ohh noo, you can't run faster than this \n Game ends......")

        if playerinput2 == "n":
            print("You coward😡, Scared of exploring ")
            print(" For you \n The game ends.......")

          
            

    else:
        print("You have been caught by a spirit named Himal(very dangerous spirit)")
        die = input("You have died because of himal, blame him 🤡 \n Press Again to restart:")
        print("You die........")


def prison():
    print(input("See what have you become, Shame of you🤥 "))
    print("You could do nothing to save yourself \n Stay and follow our words and you will be released after 1 year....")
    player_input6 = input("Press W to go against government \n Press N to follow their words and serve 1 year in prison as a prisoner:").lower().strip()
    print(player_input6)
    if player_input6 == "w":
        print("Get lost to hell and die you don't deserve to live here!  \nThis game ends.... ")

    if player_input6 == "n":
        print("Today you have to break 20 stones")
        user_input7 = input("Will you? (Y/N):   ").lower().strip()
        print(user_input7)
        if user_input7 == "y":
            print("Good👍...")
        elif user_input7 == "n":
            print("Then you won't get food 🍱.....")    


def Beautiful():
    print("Hello,\n Welcome to our beautiful place🙏 \n Be careful if you attempt to harm anything here you will be sent to Punished!")
    user_input1 = input("A bird is resting;\n catch it/eat fivestar(its in the table): ").lower().strip()
    print(user_input1)
    if user_input1 == "catch it":
        print("You went against our rules \n You will be punished and will be sent to prison")
        prison()

    elif user_input1 == "eat fivestar":
        print("You won nothing by eating 5 star ⭐️,\n (You won something, check your inventory;)")
        input4 = input("There's a gift type C to claim:")
        print(input4)
        print("You won 💩")  
        




    













def start():
    print("One dark and mysterious night, you came to understand the truth behind 2 mysterious \n doors present in your town.\n One door led to a world of happiness, while the other led to a world of danger. Nobody knew what was behind them, and the only way to find out was to choose one.")
    
    
    name = input("Enter your name:")
    print("Hello ",  name)
    
    
    print("You are stuck here!,\n choose one door to exit.")


    print("There are two Doors in opposite direction with each other.One is black and other is white")
    choice = input("You must choose one Door(B/W): ").lower().strip()
    if choice == "b":
        haunted()
    elif choice == "w":
        Beautiful()
    else:
        typed_answer = input("Try again \n Type:B/W:")

        print(typed_answer)   

            
while True:
    if do_continue=="y": 
        start()
    elif  do_continue=="n":
        break
    else:
        print("Enter a valid input")
        continue

    do_continue=input("Do you want to continue? (y/n)").lower().strip()

    
    

