#Name: Kevin Zheng
#Class: 5th Hour
#Assignment: Scenario 1


#Scenario 1:
#You are a programmer for a fledgling game developer. Your team lead
#has asked you to create a nested dictionary containing five enemy
#creatures (and their properties) for combat testing. Additionally,
#the testers are asking for a way to input changes to the enemy's
#damage for balancing, as well as having it print those changes to
#confirm they went through.

#It is up to you to decide what properties
#are important and the theme of the game.

#UPDATE: The testers have run into some bugs with your code. Some of the
#code seems to not work correctly. For example, one of the testers changed
#the damage for an enemy to 30 per attack, but when they attacked the player
#character, the health went from 100 to 10030 instead of the intended 70.
#Your team lead has asked you to fix the bug.
#(HINT: The player's health is stored as an integer.)




MonkeyDict = {
    "Diddy Kong": {
        "Health" : 10,
        "Damage" : 2,
        "Speed" : 5,
    },
    "Dixie Kong": {
        "Health" : 10,
        "Damage" : 3,
        "Speed" : 6,
    },
    "Donkey Kong": {
        "Health" : 20,
        "Damage" : 10,
        "Speed" : 3,
    },
    "King Kong" : {
        "Health" : 40,
        "Damage" : 20,
        "Speed" : 1,
    },
    "Curious George" : {
        "Health" : 100,
        "Damage" : 100,
        "Speed" : 100,
    }
}

normalized_dict = {key.strip().lower(): key for key in MonkeyDict}


def display_stats(stats):
    print("\nCurrent Character Stats:")
    for character, attributes in stats.items():
        print(f"{character}:")
        for attr, value in attributes.items():
            print(f"  {attr}: {value}")
        print()



def update_character_stats(stats):
    display_stats(stats)

    character_name = input("\nEnter the name of the character to update: ").strip().lower()
    actual_name = normalized_dict.get(character_name)

    if actual_name:
        print(f"Updating stats for {actual_name}:")
        for attr in stats[actual_name].keys():
            while True:
                try:
                    new_value = int(input(f"  Enter new value for {attr} (current value is {stats[actual_name][attr]}): "))
                    stats[actual_name][attr] = new_value
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer value.")
        print(f"Stats for {actual_name} updated successfully.")
    else:
        print("Character not found.")





def main():
    while True:
        print("\n1. Display character stats")
        print("2. Update character stats")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            display_stats(MonkeyDict)
        elif choice == "2":
            update_character_stats(
                MonkeyDict)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()







