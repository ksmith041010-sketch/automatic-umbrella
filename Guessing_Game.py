# =========================================================
# 1. IMPORTS
# =========================================================

import random


# =========================================================
# 2. GAME STATE VARIABLES (GLOBAL SETTINGS)
# =========================================================

playing = True
score = 0
DEBUG_MODE = False

current_streak = 0
best_streak = 0

round_number = 1

# Achievement tracker

achievements = []

print("Select Difficulty")
print()

print("1. Easy 💤")
print("2. Medium 🤔")
print("3. Hard 🤓")
print("4. Nightmare 😭")

while True:
    
        difficulty_choice = input("Choose difficulty (1-4): ")
        
        if difficulty_choice == "1":
            difficulty_name = "Easy"
            max_number = 25
            starting_lives = 5
            break
        
        elif difficulty_choice == "2":
            difficulty_name = "Medium"
            max_number = 50
            starting_lives = 6
            break
        
        elif difficulty_choice == "3":
            difficulty_name = "Hard"
            max_number = 100
            starting_lives = 7
            break
        
        elif difficulty_choice == "4":
            difficulty_name = "Nightmare"
            max_number = 500
            starting_lives = 8
            break
        
        else:
            print("❌ Please choose 1, 2, 3, or 4.")
            
 # =========================================================
# 3. STATS
# =========================================================           

def display_intro():
    
    gammertag = input("Enter your gammertag: ")
    print("Welcome, " + gammertag + "!")
    print()

    return gammertag

gammertag = display_intro()

def display_header(lives, hint_tokens):
    
    print()
    print("🎮", gammertag, "| Round", round_number, "|", difficulty_name)
    
    print()
    print("⭐ Score:", score)
    print("🔥 Current Streak:", current_streak)
    print("🏆 Best Streak:", best_streak)
    
    hearts = "❤️" * lives
    
    print()
    print(hearts, "🪙" + str(hint_tokens))
    
# =========================================================
# 4. SCORE & ACHIEVEMENT FUNCTIONS
# =========================================================

def add_score(amount):
    
    global score
    
    score += amount
    
    if amount > 0:
        print("➕ +" + str(amount) + " points!")
        
    elif amount < 0:
        print("➖" + str(amount) + " points")
        
def unlock_achievement(name):
        
        if name not in achievements:
            
            achievements.append(name)
            
            print()
            print("🏆 ACHIEVEMENT UNLOCKED!")
            print(name)
        
# =========================================================
# 5. MAIN GAME LOOP (ENTIRE GAME RUNS HERE)
# =========================================================

while playing:
    
    # =========================================================
    # 6. NEW ROUND SETUP
    # =========================================================
    
    lives = starting_lives
    
    hint_tokens = 1
    
    display_header(lives, hint_tokens)
    # The header is describing the round. Therefore it belongs where the round is being created. 
    
    secret = random.randint(0, max_number)
    
    if DEBUG_MODE:
        print("DEBUG:", secret)
    
    previous_distance = None
    
    print()
    
    print("Protect your hearts!")
    print("Guess a number between 0 and ", max_number)
    
    
    print()
          
    
    # =========================================================
    # 7. ATTEMPTS LOOP (GUESSES VARY BY DEGREE OF DIFFICULTY)
    # =========================================================
    
    while lives > 0:
        
        while True:
            try:
                guess = int(input("Enter your guess: "))
                
                if guess < 0 or guess > max_number:
                    print("❌ Please enter a number between 0 and", max_number)
                    
                else:
                        break
            
            except:
                print("❌ Please enter a valid number.")
        
        # =========================================================
        # 8. WIN CONDITION
        # =========================================================
        
        if guess == secret:
            print("Whoop whoop! You got it!")
            
            add_score(100)
            
            unlock_achievement("🎯 First Victory")
            
            current_streak += 1
            
            if current_streak > best_streak:
                best_streak = current_streak
                
                if best_streak == 3:
                    unlock_achievement("🔥 On Fire")
                
                print("🔥 Current Streak:", current_streak)
                print("🏆 Best Streak:", best_streak)
            
            
                
            print("⭐ Total Score:", score)    
                
            break
        # =========================================================
        # 9. WRONG GUESS FEEDBACK SYSTEM
        # =========================================================
       
        else:
            lives -= 1
            
            hearts = "❤️" * lives
            
            print("💔 You lost a heart!")
            print(hearts)
            
            distance = abs(secret - guess)
            
            # --- Hot / Cold system ---
            if distance <= 3:
                print("🔥 YOU'RE BURNING UP!")
                print("☀ Close guess bonus! +10")
                add_score(10)
                
            elif distance <= 7:
                print("🌡 You're warm!")
                
            elif distance <=15:
                print("🧊 You're cold.")
                
            else:
                print("🥶  Brr! You're freezing")
            
            # --- Hotter / colder tracking ---
            if previous_distance is not None:
                
                if distance < previous_distance:
                    print("📈 You're getting hotter!")
                
                elif distance > previous_distance:
                    print("📉 You're getting colder.")
                
                else:
                    print("➡️You're the same distance as before.")
                    
            # --- update tracker (IMPORTANT) ---
            previous_distance = distance
            
            if lives == 0:
                
                current_streak = 0
                
                print()
                print("💀 No hearts remaining!")
                print("🥁 The secret number was:", secret)
                print("⭐ Total Score:", score)
                break
    # =========================================================
    # 10. END OF ROUND (NO MORE ATTEMPTS)
    # =========================================================
    if lives == 0:
        
        current_streak = 0
        
        print()
        print("💀 No hearts remaining!")
   
        
    # =========================================================
    # 11. PLAY AGAIN LOOP
    # =========================================================
    
    while True:
        again = input("Would you like to try again? (Y/N): ").strip().lower()
    
        if again == "y":
            
            round_number += 1
            
            break # go back to top of main loop
    
        elif again == "n":
            print("Game over. À bientôt!")
            playing = False
            break
        
        else:
            print("Please enter only Y or N.")
            
        
    