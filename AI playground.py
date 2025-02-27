import random
import time

# Define Character Class with Mana, Spells, and Weapons
class Character:
    def __init__(self, name, health, attack, defense, mana, weapon=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.mana = mana
        self.max_mana = mana
        self.experience = 0
        self.level = 1
        self.weapon = weapon if weapon else None  # If no weapon is provided, default to None

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.attack += weapon.attack_modifier
        print(f"{self.name} equipped {weapon.name} and gained {weapon.attack_modifier} attack!")

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack - 5, self.attack + 5) - enemy.defense
        if damage < 0:
            damage = 0
        print(f"{self.name} attacks {enemy.name} with {self.weapon.name} for {damage} damage!")
        enemy.take_damage(damage)
        return damage

    def cast_spell(self, spell, enemy=None):
        if self.mana >= spell["mana_cost"]:
            self.mana -= spell["mana_cost"]
            if spell["type"] == "damage":
                damage = random.randint(spell["min_damage"], spell["max_damage"]) - enemy.defense
                if damage < 0:
                    damage = 0
                print(f"{self.name} casts {spell['name']} and deals {damage} damage!")
                enemy.take_damage(damage)
            elif spell["type"] == "heal":
                heal_amount = random.randint(spell["min_damage"], spell["max_damage"])
                self.health += heal_amount
                print(f"{self.name} casts {spell['name']} and heals {heal_amount} health!")
            elif spell["type"] == "buff":
                self.attack += spell["buff_amount"]
                print(f"{self.name} casts {spell['name']} and increases attack by {spell['buff_amount']}!")
            return True
        else:
            print(f"{self.name} does not have enough mana to cast {spell['name']}!")
            return False

    def gain_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience!")
        if self.experience >= 100:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.health += 20
        self.attack += 5
        self.defense += 2
        self.max_mana += 10
        self.mana = self.max_mana  # Restore mana on level up
        print(f"{self.name} leveled up! Now at level {self.level}. Health, attack, and defense increased!")

    def show_status(self):
        print(f"{self.name} - Level: {self.level} | Health: {self.health} | Attack: {self.attack} | Defense: {self.defense} | Mana: {self.mana}/{self.max_mana} | Weapon: {self.weapon.name if self.weapon else 'None'} | Experience: {self.experience}/100")


# Define Weapon Class
class Weapon:
    def __init__(self, name, attack_modifier):
        self.name = name
        self.attack_modifier = attack_modifier


# Define Enemy Class
class Enemy:
    def __init__(self, name, health, attack, defense, experience_reward):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.experience_reward = experience_reward

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def attack_player(self, player):
        damage = random.randint(self.attack - 5, self.attack + 5) - player.defense
        if damage < 0:
            damage = 0
        print(f"{self.name} attacks {player.name} for {damage} damage!")
        player.take_damage(damage)
        return damage


# Game Setup and Main Loop
def main():
    print("Welcome to the Turn-Based RPG Game with Weapons and Spells!\n")

    # Create Player
    player_name = input("Enter your character's name: ")
    player = Character(player_name, health=100, attack=20, defense=5, mana=50)

    # Define Weapons
    sword = Weapon(name="Sword", attack_modifier=10)
    bow = Weapon(name="Bow", attack_modifier=7)
    staff = Weapon(name="Staff", attack_modifier=5)

    # Equip Weapon
    player.equip_weapon(sword)  # The player starts with a sword

    # Define Spells
    fireball = {"name": "Fireball", "type": "damage", "mana_cost": 10, "min_damage": 20, "max_damage": 40}
    heal = {"name": "Heal", "type": "heal", "mana_cost": 15, "min_damage": 15, "max_damage": 30}
    buff_attack = {"name": "Power Boost", "type": "buff", "mana_cost": 12, "buff_amount": 5}

    spells = [fireball, heal, buff_attack]

    # Game loop
    while player.is_alive():
        player.show_status()

        # Randomly select an enemy for the player to fight
        enemy_type = random.choice(["Goblin", "Orc", "Dragon"])

        if enemy_type == "Goblin":
            enemy = Enemy(name="Goblin", health=50, attack=10, defense=2, experience_reward=30)
        elif enemy_type == "Orc":
            enemy = Enemy(name="Orc", health=80, attack=15, defense=5, experience_reward=50)
        else:
            enemy = Enemy(name="Dragon", health=120, attack=25, defense=8, experience_reward=100)

        print(f"\nA wild {enemy.name} has appeared!")

        # Turn-based combat loop
        while enemy.is_alive() and player.is_alive():
            # Player's turn
            print("\nYour turn:")
            action = input("What will you do? (Attack/Rest/Cast Spell): ").lower()

            if action == "attack":
                player.attack_enemy(enemy)
                time.sleep(1)
            elif action == "rest":
                heal = random.randint(10, 20)
                player.health += heal
                print(f"You rested and regained {heal} health.")
                time.sleep(1)
            elif action == "cast spell":
                print("Available Spells:")
                for idx, spell in enumerate(spells):
                    print(f"{idx + 1}. {spell['name']} (Cost: {spell['mana_cost']} Mana)")
                spell_choice = int(input(f"Choose a spell (1-{len(spells)}): ")) - 1

                if 0 <= spell_choice < len(spells):
                    spell = spells[spell_choice]
                    player.cast_spell(spell, enemy)
                else:
                    print("Invalid choice!")
                time.sleep(1)
            else:
                print("Invalid action! You can either 'Attack', 'Rest', or 'Cast Spell'.")
                continue

            if not enemy.is_alive():
                print(f"\nYou defeated the {enemy.name}!")
                player.gain_experience(enemy.experience_reward)
                break

            # Enemy's turn
            print(f"\n{enemy.name}'s turn:")
            enemy.attack_player(player)
            time.sleep(1)

            if not player.is_alive():
                print("\nYou have been defeated!")
                break

        # After battle, offer the player a chance to rest
        if player.is_alive():
            rest = input("\nDo you want to rest and recover some health? (y/n): ").lower()
            if rest == 'y':
                heal = random.randint(10, 30)
                player.health += heal
                print(f"\nYou rested and regained {heal} health!")
            else:
                print("\nYou decided not to rest and continue your journey.")

        # Random event (Chance for a mini-quest)
        if random.random() < 0.2:
            print("\nA wandering merchant offers to sell you healing potions.")
            buy = input("Do you want to buy a healing potion for 20 gold? (y/n): ").lower()
            if buy == 'y':
                print("\nYou bought a healing potion and regained 50 health!")
                player.health += 50

    print("\nGame Over!")
    print(f"{player.name}'s final level: {player.level} | Final score: {player.experience} experience")


if __name__ == "__main__":
    main()
