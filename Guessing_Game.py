import random

secret = random.randint(18,50)
print("DEBUG:", secret)

while True: # <- keeps the whole game running
    for i in range(3):
        print("Attempt", i + 1)
    
        guess = int(input("You only have 3 tries. Make them count. Guess a number between 0 and 20: "))
    
        if guess == secret:
            print("Whoop whoop!")
            break
        else:
            print("Sad face")
    else:
        print("Out of tries")
    
    #NEW PART
    again = input("Would you like to try again? (Yes/No): ")

    if again.lower() == "no":
        print("Game over. À bientôt!")
        break

    

              
        