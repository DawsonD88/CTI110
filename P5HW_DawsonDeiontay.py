# Deiontay Dawson
# 14 July 2025
# P5HW_DawsonDeiontay
# Create your own Adventure Game

#import modules
import random

#global variables
score = 0
corr_ans = 0
characters = {}

# Simulated user name for non-interactive environments
name = input("Please enter you name: ")
player = name

#define user-functions

#define dice to random integer to determine health decrease
def roll_dice():
    return random.randint(1, 6)
#define coin toss to guess probability
def coin_toss():
    return random.choice(["heads", "tails"])
#define input to allow program to run through error
def safe_input(prompt, fallback=""):
    try:
        return input(prompt)
    except OSError:
        return fallback
#define character attributes with health and score by num of corr answers
def character(corr_ans, health):
    guess = safe_input("Guess the coin toss (heads/tails): ", fallback="heads").lower()
    actual = coin_toss()
    print(f"Coin toss result: {actual}")

    if guess == actual:
        corr_ans += 1
        print("You guessed correctly — Correct answer counted.")
    else:
        dice = roll_dice()
        if dice % 2 == 0:
            health != 0
            print(f"Dice roll: {dice} (even)")
        else:
            health -= 10
            print(f"Dice roll: {dice} (odd) — Health decreased by 10.")
        print("Wrong guess — No correct answer this time.")
    #Score Calculation
    score = corr_ans * health
    #Dictionary
    char_info = {
        "name": name,
        "health": health,
        "correct_answers": corr_ans,
        "score": score
    }

    print(f"Your score is now {score}.")
    print(f"Your health is at {health}%")
    if health <= 0:
        print(f"Your health is {health}%.")
        print("You have lost the game.")

    characters[name] = {
        "score": score,
        "correct_answers": corr_ans
    }

    return char_info
#Define main function
def main():
    global corr_ans
    print(f"Welcome to Ebony's Playground {player}!!")
    print("=" * 66)
    print("              This is where your adventure begins!              ")
    print("=" * 66)
    print("You will be given choices to make as you navigate through the game.")
    print("Let's start your adventure!")
    health = 100
    while health > 0: #Start loop
        character_data = character(corr_ans, health)
        corr_ans = character_data["correct_answers"]
        health = character_data["health"]

        if health <= 0:
            break

        proceed = safe_input("Press Enter to continue or type 'quit' to exit: ", fallback="").lower()
        if proceed == 'quit':
            break

    print(f"\n{player}, your adventure has ended. Your final score is {character_data['score']}")
    print(f"Thank you for playing, {player}! Goodbye!") #end loop

    print("\nCharacter Summary:")
    for char_name, info in characters.items(): #print Values of Dictionary
        print(f"Name: {char_name}, Score: {info['score']}, Correct Answers: {info['correct_answers']}")

if __name__ == '__main__':
    main()
    
