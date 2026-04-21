playing = True
import random

while playing:
    secret = random.randint(0,50)
    print("DEBUG:", secret)
    previous_distance = None
    for i in range(5):
        print("Attempt", i + 1)
    
        guess = int(input("You have 5 attempts to guess the secret number. Make them count. Guess a number between 0 and 50: "))
    
        if guess == secret:
            print("Whoop whoop! You got it!")
            break
        else:
            distance = abs(secret - guess)
            
            # First feedback (hot/cold)
            if distance <= 3:
                print("🔥 YOUR BURNING UP!")
            elif distance <= 7:
                print("🌡 You're warm!")
            elif distance <=15:
                print("🧊 You're cold.")
            else:
                print("🥶  Brr! You're freezing")
            
            # Hotter / colder tracking
            if previous_distance is not None:
                if distance < previous_distance:
                    print("📈 You're getting hotter!")
                elif distance > previous_distance:
                    print("📉 You're getting colder.")
                else:
                    print("➡️You're the same distance as before.")
                    
            # update tracker
            previous_distance = distance
    else:
        print("Out of tries")
    
    while True:
        again = input("Would you like to try again? (Y/N): ").strip().lower()
    
        if again == "y":
            break # go back to top of main loop
    
        elif again == "n":
            print("Game over. À bientôt!")
            playing = False
            break
        
        else:
            print("Please enter only Y or N.")
            break
        
