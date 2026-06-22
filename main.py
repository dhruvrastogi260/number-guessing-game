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

def lod_to_chances():
    while True :
        lod = (input(f"\nEnter level of difficulty: "))

        try:
            if int(lod) == 1:
                return 15,"easy"

            elif int(lod) == 2:
                return 10,"medium"
                

            elif int(lod) == 3:
                return 5,"hard"
                
            else :
                print("an error occured\nPlease")
        except ValueError:
            print("an error occured\nPlease")
        

while True:
    number = random.randint(1,100)

    chances,level = lod_to_chances()

    print(f"Great! your level is {level} with {chances} chances,\nLet's start the game!")

    for i in range(1,(chances+1)):
        while True:
            try:
                guess = int(input("\nenter your guess: "))
                break
            except ValueError:
                print("Please enter a number for the guess")

        if guess == number:
            print(f"you win!!!\nIn {i} attempts")
            break

        elif guess > number:
            print(f"you need to guess lower")
            
        elif guess < number:
            print(f"you need to guess higher")

    else:
        print(f"you loser\ncan\'t even guess in {i}")


    while True :
        rematch = input("\ndo you wanna rematch \nIf yes send \'y\'\nIf no send\'n\' \n????: ")
        if rematch in ["y","n","yes","no"]:
            break
        else:
            print("give a valid response that i understand")

    if rematch.lower() == "y" or rematch.lower() == "yes":
        continue
    elif rematch.lower() == "n" or rematch.lower() == "no" :
        print("okay byee")
        break
