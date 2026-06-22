import random

print(""" 
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have limited chances to guess the correct number.

Please select the difficulty level:
1. Easy (15 chances)
2. Medium (10 chances)
3. Hard (5 chances)
""")

def lod_to_chances(a = ""):

    global lod

    global gamemode

    lod = (input(f"\nEnter {a}level of difficulty: "))

    try:
        if int(lod) == 1:
            lod = 15
            gamemode = "easy with 15 chances"

        elif int(lod) == 2:
            lod = 10 
            gamemode = "medium with 10 chances"

        elif int(lod) == 3:
            lod = 5
            gamemode = "hard with 5 chances"

        else:
            lod_to_chances("valid ")

    except ValueError:
        print("an error occured\nPlease")
        lod_to_chances("valid ")

while True:
    number = random.randint(1,100)

    lod_to_chances()

    print(f"Great! your level is {gamemode}\nLet's start the game!")

    for i in range(1,int(lod)+1):
        guess = int(input("\nenter your guess: "))
        if guess == number:
            print(f"you win!!!\nIn {i} attempts")
            break
        elif guess > number:
            print(f"you need to guess lower")
            
        elif guess < number:
            print(f"you need to guess higher")
    else:
        print(f"you loser\ncan\'t even guess in {i}")

    rematch = input("\ndo you wanna rematch \nIf yes send \'y\'\nIf no send\'n\' \n????: ")

    if rematch.lower() == "y" or rematch.lower() == "yes":
        continue
    elif rematch.lower() == "n" or rematch.lower() == "no" :
        print("okay byee")
        break
