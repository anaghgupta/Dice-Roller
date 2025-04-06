import random

def roll_dice():
    return random.randint(1, 6)

print("🎲 Welcome to the Dice Roller Simulator!")
while True:
    input("Press Enter to roll the dice...")
    result = roll_dice()
    print(f"You rolled a {result}!\n")

    again = input("Do you want to roll again? (y/n): ").lower()
    if again != 'y':
        print("Thanks for playing! Goodbye 👋")
        break
