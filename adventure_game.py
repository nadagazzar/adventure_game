import time
import random


def slow_print(text):
    #Prints text slowly  for a narrative effect.
    print(text)
    time.sleep(1)

def get_location_choice():
    #Asks the player to choose a location and ensures it's valid.
    valid_choices = ['1', '2', '3']
    choice = None
    while choice not in valid_choices:
        choice = input("Choose a location: (1 , 2 , 3 ): ")
        if choice not in valid_choices:
            print("Invalid choice. Please choose 1, 2, or 3.")
    return choice

def get_interaction_choice():
    #Asks the player whether to fight or run
    valid_choices = ['fight', 'run']
    choice = None
    while choice not in valid_choices:
        choice = input("Do you want to fight or run? ")
        if choice not in valid_choices:
            print("Invalid choice. Please type 'fight' or 'run'.")
    return choice


def encounter(level):
    enemies = [
        "a wild gorilla", "a giant snake", "a jungle bandit",
        "a massive spider", "a swarm of wasps"
    ]
    enemy = random.choice(enemies)
    slow_print(f"\nYou encounter {enemy}!")

    action = get_interaction_choice()

    if action == "fight":
        # It becomes harder with each level
        fight_chance = 0.5 - (level * 0.05)
        if random.random() < fight_chance:
            slow_print("You fought bravely and won!")
            return True
        else:
            slow_print("You were defeated in the fight...")
            return False
    else:  
        # The player chose the 'run' option
        if random.random() < 0.3:
            slow_print("You tried to run but fell into a trap!")
            return False
        else:
            slow_print("You escaped safely!")
            return True


def play_level(level, health):
    #The treasure value increases each level
    slow_print(f"\n LEVEL {level} - A new challenge awaits...")
    treasure_location = random.choice(["house", "cave", "forest"])
    treasure_value = random.randint(500 + level * 50, 1000 + level * 100)
    treasure_found = False

    while health > 0 and not treasure_found:
        # Ask the player where they want to go
        slow_print("\nWhere do you want to go?")
        slow_print("1. House\n2. Cave\n3. Forest")
        location_choice = get_location_choice()
        location = ["house", "cave", "forest"][int(location_choice) - 1]

        # Check if treasure is in that location
        if location == treasure_location:
            slow_print(f"\n You found the treasure worth {treasure_value} coins!")
            treasure_found = True
            continue

        # If not, player encounters danger
        result = encounter(level)
        if not result:
            health = 0  # Player dies
        else:
            #Chance to recover some health
            recovery = random.randint(0, 10)
            if recovery > 0:
                slow_print(f"You found some berries and recovered {recovery} health!")
                health += recovery

        slow_print(f"Your current health: {health}")

    # Return updated health and alive statues
    if treasure_found and health > 0:
        slow_print(f"\nLEVEL {level} COMPLETE!")
        return health, True
    else:
        slow_print("\n You have perished in the jungle.")
        return health, False


def play_game():
    
    #key variables
    health = 100
    level = 1
    max_level = 5  
    slow_print(" Welcome to the Jungle Adventure Game!")
    slow_print("Survive 5 levels, find treasure, and escape the jungle!")

    while health > 0 and level <= max_level:
        health, alive = play_level(level, health)
        if not alive:
            break  

        if level == max_level:
            #Ending the game when completing five levels
            slow_print("\n Congratulations! You completed all 5 levels and escaped the jungle with treasure!")
            return
        level += 1
        slow_print(f"Preparing for Level {level}...\n")

    if health <= 0:
        slow_print(" Game over....")


#play again option
while True:
    play_game()
    play_again = input("\nDo you want to play again? (y/n): ").lower()
    if play_again not in ["y","yes"]:
        slow_print("Thanks for playing!")
        break