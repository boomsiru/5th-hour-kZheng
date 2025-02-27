import math
import random
import time

EnemyAccuracy = 0
EnemyLevel = 0
EnemiesKilled = 0
EnemiesLeft = 0
Turn = 0
floorLevel = -1
EnemyDamage = 0
EnemySpeed = 0
EnemyStrength = 0
EnemyDefense = 0
EnemyMagic = 0
EnemyHealth = 0
gotDeathBlowed = False
EnemyPoisoned = False
EnemyFrozen = False
EnemyIchored = False
EnemyBurned = False
EnemyAcidified = False
EnemyStunned = False
acidSpellUnlocked = False
praySpellUnlocked = False
poisonTurn = None
freezeTurn = None
ichorTurn = None
burnTurn = None
acidTurn = None
stunTurn = None
playerHealing = False
healTurn = None
playerBurned = False
playerBurnTurn = None
InfinityActivated = False
ExplosionsUsed = 0
Speed = 0
Strength = 0
Defense = 0
Magic = 0
Mana = None
maxMana = None
Health = 0
maxHealth = 0
startHealth = 0
CritChance = 0.05
XP = 0
baseXP = 10
growthFactor = 5
Level = 1
nextLevel = 10
points = 0
Accuracy = 0
BaseAccuracy = 0.85
LevelAccuracy = 0.01
runChance = 0
item = None
itemsCollected = 0
potion = None
weapon = None
weaponStrength = 0
weaponMagic = 0
weaponDefense = 0
weaponSpeed = 0
Ressurection = False
money = 0
maxMoney = 1

print("Welcome to my RPG. Your goal is to escape the dungeon.")
print("If you have the same speed as an enemy, the enemy will attack first.")
print("Enemies also have a chance to attack after they die as a last-ditch effort.")
print("These attacks are called deathblows.")
print("If you have an option that says (y), you can cancel or decline by typing anything but y.")
AnimeSpecs = input("Do you want to play with anime items? (y): ")
Start = input("Press enter to begin. ")
print("")
Enemy = False


def adjust_weapon_stats(adding=True):
    global Strength, Magic, Defense, Speed, weapon, CritChance, Accuracy

    weapon_modifiers = {
        "Strength": {"Strength": 2},
        "Magic": {"Magic": 2},
        "Speed": {"Speed": 2},
        "Defense": {"Defense": 2},
        "Cursed Energy": {"Speed": 2, "Magic": 3},
        "Gambling Cursed Energy": {"Accuracy": 0.25, "CritChance": 0.2},
        "Luck": {"Accuracy": 0.15, "CritChance": 0.1},
        "Better Magic": {"Magic": 4},
        "Fishman": {"Speed": 2, "Strength": 2, "Magic": 2},
        "Everything": {"Accuracy": 0.1, "CritChance": 0.1, "Speed": 1, "Strength": 1, "Magic": 1, "Defense": 1},
        "Ki": {"Strength": 2, "Magic": 2, "Speed": 2, "Defense": 2}
    }

    modifier = 1 if adding else -1

    if weapon in weapon_modifiers:
        for stat, increase in weapon_modifiers[weapon].items():
            globals()[stat] += modifier * (Level + increase)


def get_hit_chance(accuracy, level):
    return accuracy + (level * LevelAccuracy)


def upgrade_stat(stat_name, stat_value, points, cost_multiplier=1, upgrade_multiplier=1):
    while True:
        times_upgraded = input(f"Pick an amount of times to upgrade {stat_name}: ")
        try:
            times_upgraded = int(times_upgraded)
            break
        except ValueError:
            print("That is not a valid number. Please enter a valid integer.")

    upgrade_cost = times_upgraded * cost_multiplier
    if points >= upgrade_cost:
        stat_value += times_upgraded * upgrade_multiplier
        if stat_name == "Max Health":
            global Health
            Health += times_upgraded * upgrade_multiplier
        points -= upgrade_cost
        print(f"You upgraded {stat_name}. You now have {stat_value} {stat_name.lower()}.")
        if stat_name == "Max Health":
            print(f"You now have {Health} health.")
    else:
        print("You don't have enough points.")

    return stat_value, points


def XPcheck():
    global XP, nextLevel, Level, maxHealth, Health, Strength, Defense, Magic, Speed, growthFactor, baseXP, points, Mana, maxMana
    if nextLevel <= XP:
        while nextLevel <= XP:
            Level += 1
            nextLevel += baseXP + (Level ** 2) * growthFactor
            points += 3
            adjust_weapon_stats(False)
            statChance = random.randint(1, 10)
            if statChance == 1:
                Strength += 2
            else:
                Strength += 1
            statChance = random.randint(1, 10)
            if statChance == 1:
                Defense += 2
            else:
                Defense += 1
            statChance = random.randint(1, 10)
            if statChance == 1:
                Magic += 2
            else:
                Magic += 1
            statChance = random.randint(1, 10)
            if statChance == 1:
                Speed += 2
            else:
                Speed += 1
            statChance = random.randint(1, 10)
            if statChance == 1:
                maxHealth += 2
                Health += 2
            else:
                maxHealth += 1
                Health += 1
        print(f"You leveled up! You are now level {Level}!")
        print("")
        print("You get upgrade to all stats.")
        print("Upgrading HP costs 2 points and everything else is 1.")
        maxMana += Magic
        Mana += Magic
        print("")
        print("Current stats:")
        print(f"Health/Max health: {Health}/{maxHealth}")
        print(f"Speed: {Speed}")
        print(f"Strength: {Strength}")
        print(f"Defense: {Defense}")
        print(f"Magic: {Magic}")
        print(f"Mana/Max mana: {Mana}/{maxMana}")
        print("")
        while points > 0:
            print(f"You have {points} points left.")
            use_points = input("Pick one of (Spd/Str/Df/Mgc/HP/None): ").lower()

            if use_points == "spd":
                Speed, points = upgrade_stat("Speed", Speed, points)
            elif use_points == "str":
                Strength, points = upgrade_stat("Strength", Strength, points, cost_multiplier=1, upgrade_multiplier=2)
            elif use_points == "df":
                Defense, points = upgrade_stat("Defense", Defense, points)
            elif use_points == "mgc":
                Magic, points = upgrade_stat("Magic", Magic, points)
            elif use_points == "hp":
                maxHealth, points = upgrade_stat("Max Health", maxHealth, points, cost_multiplier=2,
                                                 upgrade_multiplier=3)
            elif use_points == "none":
                print("Choosing to upgrade nothing saves your points, but you might struggle incoming fights.")
                ensurePlayer = input("Are you sure you want to do this? (y): ")
                if ensurePlayer.lower() == "y":
                    print("You chose to save the rest of your points.")
                    print(f"You have {points} points left.")
                    break
            else:
                print("That is not an option.")
            print("")
        else:
            if item == "Weapon":
                adjust_weapon_stats(True)
            print("")
            print("New stats:")
            print(f"Health/Max health: {Health}/{maxHealth}")
            print(f"Speed: {Speed}")
            print(f"Strength: {Strength}")
            print(f"Defense: {Defense}")
            print(f"Magic: {Magic}")
            print("")


def deathblow(Chance):
    global Health, EnemyDamage, EnemyAccuracy, EnemyLevel, gotDeathBlowed
    if Chance != 1:
        print("The enemy is doing a deathblow.")
        time.sleep(1)
        enemy_hit_chance = get_hit_chance(EnemyAccuracy, EnemyLevel)
        if random.random() <= enemy_hit_chance:
            Health -= EnemyDamage
            if Health < 0:
                Health = 0
            print(f"The {Enemy} did {EnemyDamage} damage with its deathblow. You are now at {Health} health.")
            if Health == 0:
                gotDeathBlowed = True
        else:
            print(f"The {Enemy} missed its deathblow.")
        time.sleep(1)


def EnemyCheck():
    global Enemy, EnemySpeed, EnemyStrength, EnemyDefense, EnemyMagic, EnemyHealth, EnemyAccuracy, EnemyLevel
    print("")
    if EnemyLevel < 5:
        Chance = random.randint(1, 10)
    elif EnemyLevel < 10:
        Chance = random.randint(1, 20)
    elif EnemyLevel < 20:
        Chance = random.randint(1, 30)
    else:
        Chance = 1
    if Chance <= 5:
        Enemy = "Slime"
        print("You have encountered a slime.")
        time.sleep(0.5)
        EnemySpeed = random.randint(1, 2) + EnemyLevel
        EnemyStrength = random.randint(1, 3) + EnemyLevel
        EnemyDefense = random.randint(1, 2) + EnemyLevel
        EnemyMagic = random.randint(2, 4) + EnemyLevel
        EnemyAccuracy = 0.6
        EnemyHealth = 3 + EnemyLevel
    elif Chance <= 10:
        Enemy = "Skeleton"
        print("You have encountered a skeleton.")
        time.sleep(0.5)
        EnemySpeed = random.randint(3, 5) + EnemyLevel
        EnemyStrength = random.randint(1, 5) + EnemyLevel
        EnemyDefense = random.randint(1, 2) + EnemyLevel
        EnemyMagic = random.randint(1, 2) + EnemyLevel
        EnemyAccuracy = 0.8
        EnemyHealth = 3 + EnemyLevel
    elif Chance <= 15:
        Enemy = "Goblin"
        print("You have encountered a mind goblin.")
        time.sleep(0.5)
        EnemySpeed = random.randint(3, 5) + EnemyLevel
        EnemyStrength = random.randint(3, 6) + EnemyLevel
        EnemyDefense = random.randint(2, 3) + round(EnemyLevel / 2)
        EnemyMagic = random.randint(2, 4) + EnemyLevel
        EnemyAccuracy = 0.75
        EnemyHealth = 5 + EnemyLevel
    elif Chance <= 20:
        Enemy = "Spider"
        print("You have encountered a spider.")
        EnemySpeed = random.randint(6, 9) + EnemyLevel
        EnemyStrength = random.randint(1, 2) + round(EnemyLevel / 2)
        EnemyDefense = random.randint(1, 3) + round(EnemyLevel * 0.67)
        EnemyMagic = EnemyStrength
        EnemyAccuracy = 1
        EnemyHealth = 5 + EnemyLevel
    elif Chance <= 25:
        Enemy = "Mimic"
        print("You have encountered a mimic.")
        EnemySpeed = random.randint(1, 3) + EnemyLevel
        EnemyStrength = random.randint(4, 7) + EnemyLevel
        EnemyDefense = random.randint(5, 7) + EnemyLevel
        EnemyMagic = random.randint(1, 4) + EnemyLevel
        EnemyAccuracy = 0.75
        EnemyHealth = 8 + EnemyLevel
    elif Chance <= 30:
        Enemy = "Funny Looking Lizard"
        print("You have encountered a funny looking lizard.")
        EnemySpeed = random.randint(3, 5) + EnemyLevel
        EnemyStrength = random.randint(4, 8) + EnemyLevel
        EnemyDefense = random.randint(2, 4) + EnemyLevel
        EnemyMagic = random.randint(1, 2) + EnemyLevel
        EnemyAccuracy = 0.85
        EnemyHealth = 8 + EnemyLevel
    if Enemy:
        print(
            f"The {Enemy}'s stats are speed: {EnemySpeed}, strength: {EnemyStrength}, defense: {EnemyDefense}, magic: {EnemyMagic}, health: {EnemyHealth}.")
        time.sleep(1)
        print("")


def itemGive(lootTier):
    global item, potion, weapon, Strength, Magic, itemsCollected, Speed, Defense
    itemsCollected += 1
    newitem = random.randint(1, (1 + (lootTier * 2)))
    if newitem == 1:
        newpotion = random.randint(1, 6)
        if newpotion == 1:
            newpotion = "Health"
        elif newpotion == 2:
            newpotion = "Mana"
        elif newpotion == 3:
            newpotion = "Strength"
        elif newpotion == 4:
            newpotion = "Defense"
        elif newpotion == 5:
            newpotion = "Magic"
        elif newpotion == 6:
            newpotion = "Speed"
        print(f"You found a {newpotion} potion!")
        newitem = "Potion"
    elif newitem == 2:
        print("You found a weapon!")
        newitem = "Weapon"
        if lootTier == 1:
            newWeapon = random.randint(1, 4)
        elif lootTier == 2:
            newWeapon = random.randint(1, 5)
        elif lootTier == 3:
            newWeapon = random.randint(1, 8)
        if newWeapon == 1:
            print("It was a strength enhancing weapon!")
            newWeapon = "Strength"
        elif newWeapon == 2:
            print("It was a magic enhancing weapon!")
            newWeapon = "Magic"
        elif newWeapon == 3:
            print("It was a speed enhancing weapon!")
            newWeapon = "Speed"
        elif newWeapon == 4:
            print("It was a defense enhancing weapon!")
            newWeapon = "Defense"
        elif newWeapon == 5:
            if AnimeSpecs:
                print("It was Hikari's energy!")
                newWeapon = "Gambling Cursed Energy"
            else:
                print("It was a luck enhancing weapon!")
                newWeapon = "Luck"
        elif newWeapon == 6:
            if AnimeSpecs:
                print("It was Gojo's energy!")
                newWeapon = "Cursed Energy"
            else:
                print("It was an even stronger magic enhancing weapon!")
                newWeapon = "Better Magic"
        elif newWeapon == 7:
            if AnimeSpecs:
                print("It was Za Water!!?")
                newWeapon = "Fishman"
            else:
                print("It was an everything enhancing weapon!")
                newWeapon = "Everything"
        elif newWeapon == 8:
            if AnimeSpecs:
                print("It's Goku?")
                newWeapon = "Ki"
    elif newitem == 3:
        print("You found a bag of money!")
        newitem = "Money Bag"
    elif newitem == 4:
        print("You found a phoenix feather!")
        newitem = "Phoenix Feather"
    elif newitem == 5:
        print("You found a XP potion!")
        newitem = "Potion"
        newpotion = "XP"
    elif newitem == 6:
        print("You found a senzu bean!")
        newitem = "Senzu Bean"
    elif newitem == 7:
        print("You found flamingo wings")
        newitem = "Flamingo Wings"
    time.sleep(1)

    if item is None:
        item = newitem
        if item == "Weapon":
            weapon = newWeapon
            adjust_weapon_stats(True)
        elif item == "Potion":
            potion = newpotion
    else:
        print(f"You already have an item. You have a {item}.")
        if item == "Potion":
            print(f"It is a {potion.lower()} potion.")
        elif item == "Weapon":
            print(f"It is a {weapon.lower()} enhancing weapon.")
        if newitem == "Potion":
            replaceItem = input(f"Would you like to replace it with a {newpotion.lower()} potion? (y): ")
        elif newitem == "Weapon":
            replaceItem = input(f"Would you like to replace it with a {newWeapon.lower()} enhancing weapon? (y): ")
        else:
            replaceItem = input(f"Would you like to replace it with a {newitem.lower()}? (y): ")
        if replaceItem == "y":
            adjust_weapon_stats(False)
            item = newitem
            if item == "Weapon":
                weapon = newWeapon
                adjust_weapon_stats(True)
            elif item == "Potion":
                potion = newpotion
        time.sleep(1)


def playerAttacks(Damage, AttackType):
    global EnemyHealth, EnemiesKilled, Level, CritChance
    if Damage > 0:
        didCrit = False
        critChance = random.random()
        if critChance <= CritChance:
            Damage *= 2
            didCrit = True
            if CritChance == 1:
                CritChance = 0.05
        time.sleep(1)
        if AttackType != "spd":
            player_hit_chance = get_hit_chance(Accuracy, Level)
            if didCrit:
                print("You got a critical hit!")
            Hit = random.random()
            if Hit <= player_hit_chance:
                EnemyHealth -= Damage
                if EnemyHealth < 0:
                    EnemyHealth = 0
                print(f"You did {Damage} damage, the {Enemy} is now at {EnemyHealth} health.")
            else:
                print("You missed.")
        else:
            EnemyHealth -= Damage
            if didCrit:
                print("You got a critical hit!")
            if EnemyHealth < 0:
                EnemyHealth = 0
            print(f"You did {Damage} damage, the {Enemy} is now at {EnemyHealth} health.")
        if EnemyHealth == 0:
            EnemiesKilled += 1
            deathblow(random.randint(1, 2))
    else:
        if AttackType.lower() == "spd":
            print("You failed the attack.")
        else:
            print("You are not attacking.")
    time.sleep(1)


def enemyAttacks(EnemyDamage):
    global Health, EnemyAccuracy, EnemyLevel, Enemy
    statuses()
    if EnemyDamage > 0:
        time.sleep(1)
        enemy_hit_chance = get_hit_chance(EnemyAccuracy, EnemyLevel)
        HitChance = random.random()
        if HitChance <= enemy_hit_chance:
            critChance = random.randint(1, 20)
            if critChance == 1:
                EnemyDamage *= 2
                print(f"The {Enemy} got a critical hit!")
            Health -= EnemyDamage
            if Health < 0:
                Health = 0
            print(f"The {Enemy} did {EnemyDamage} damage, you are now at {Health} health.")
        else:
            print(f"The {Enemy} missed.")
    else:
        print(f"The {Enemy} is not attacking.")
    time.sleep(1)


def doAttack(Damage, EnemyDamage, AttackType):
    time.sleep(0.5)
    if Speed > EnemySpeed:
        print(f"You have more speed than the {Enemy}. You are attacking first.")
        playerAttacks(Damage, AttackType)
        if EnemyHealth > 0:
            enemyAttacks(EnemyDamage)
    else:
        print(f"The {Enemy} has more speed than you, it is attacking first.")
        enemyAttacks(EnemyDamage)
        if Health > 0:
            playerAttacks(Damage, AttackType)


def apply_potion_effects(potion_type):
    global Health, maxHealth, XP, nextLevel, Strength, Defense, Magic, Speed, Mana, maxMana, item, potion
    if potion_type == "Health":
        if Health < maxHealth:
            Health = maxHealth
            print(f"You have used your Health Potion. You are now at {Health} health.")
        else:
            usepot = input("You are already at max health. Would you like to use your Health Potion anyway? (y): ")
            if usepot == "y":
                item = None
                potion = None
    elif potion_type == "Mana":
        if Mana < maxMana:
            Mana = maxMana
            print(f"You have used your Mana Potion. You are now have {Mana} mana.")
        else:
            usepot = input("You are already at max mana. Would you like to use your Mana Potion anyway? (y): ")
            if usepot == "y":
                item = None
                potion = None

    elif potion_type == "XP":
        XP = nextLevel
        XPcheck()
        item = None
        potion = None
    elif potion_type == "Strength":
        Strength += math.floor(Strength * 0.06)
        item = None
        potion = None
        return f"Your Strength was increased. New Strength: {Strength}"
    elif potion_type == "Defense":
        Defense += math.floor(Defense * 0.06)
        item = None
        potion = None
        return f"Your Defense was increased. New Defense: {Defense}"
    elif potion_type == "Magic":
        Magic += math.floor(Magic * 0.06)
        item = None
        potion = None
        return f"Your Magic was increased. New Magic: {Magic}"
    elif potion_type == "Speed":
        Speed += math.floor(Speed * 0.06)
        item = None
        potion = None
        return f"Your Speed was increased. New Speed: {Speed}"
    else:
        return f"You don't have a {potion_type} potion."


def useSpell():
    global Mana, Magic, Defense, EnemyDamage, CritChance, Turn, Strength, maxHealth, Health, Speed, EnemyHealth, Damage, Level
    global EnemyFrozen, EnemyPoisoned, EnemyIchored, EnemyBurned, EnemyAcidified, EnemyStunned
    global playerHealing, healTurn, playerBurned, playerBurnTurn
    global ichorTurn, freezeTurn, burnTurn, poisonTurn, stunTurn, InfinityActivated, acidSpellUnlocked, ExplosionsUsed

    if item == "Sukuna":
        Cleave = True
        Dismantle = True
        MalevolentShrine = True
        Fuga = True
    else:
        Cleave = False
        Dismantle = False
        MalevolentShrine = False
        Fuga = False

    CritSpell = Magic >= 3
    HealOverTimeSpell = Magic >= 6 and Level >= 1
    FreezeSpell = Magic >= 6 and Level >= 1
    PoisonSpell = Magic >= 6 and Level >= 1
    IchorSpell = Magic >= 9 and Level >= 2
    ExplosionSpell = Magic >= 9 and Level >= 2
    AcidSpell = acidSpellUnlocked
    PraySpell = praySpellUnlocked
    if item != "Sukuna":
        Fuga = ExplosionsUsed >= 5 and Level >= 3
    Infinity = Magic >= 30 and weapon == "Cursed Energy" and Level >= 5
    HollowPurple = Magic >= 40 and weapon == "Cursed Energy" and Level >= 5
    InfiniteVoid = Magic >= 45 and weapon == "Cursed Energy" and Level >= 5
    GalaxyImpact = Strength >= 35 and weapon == "Fishman" and Level >= 4
    FishmanMartialArts = Strength >= 10 and weapon == "Fishman" and Level >= 2
    GangnumStyle = Strength >= 10 and weapon == "Fishman" and Level >= 2
    Kamehameha = Strength and Magic >= 5 and weapon =="Ki" and Level >= 2

    # make fishman hit the gangnum style fr fr

    print("\nYou have:")
    time.sleep(0.5)
    if CritSpell:
        print("Crit Spell (Crit)")
        time.sleep(0.3)
    if HealOverTimeSpell:
        print("Heal Over Time Spell (Heal)")
        time.sleep(0.3)
    if FreezeSpell:
        print("Freeze Spell (Freeze)")
        time.sleep(0.3)
    if PoisonSpell:
        print("Poison Spell (Poison)")
        time.sleep(0.3)
    if IchorSpell:
        print("Ichor Spell (Ichor)")
        time.sleep(0.3)
    if AcidSpell:
        print("Acid Spell (Acid)")
        time.sleep(0.3)
    if ExplosionSpell:
        print("Explosion Spell (Explosion)")
        time.sleep(0.3)
    if Fuga and item != "Sukuna":
        print("Fuga (Fuga)")
        time.sleep(0.3)
    if PraySpell:
        print("Pray (Pray)")
        time.sleep(0.3)
    if Infinity:
        print("Infinity (Infinity)")
        time.sleep(0.2)
    if HollowPurple:
        print("Hollow Purple (Purple)")
        time.sleep(0.2)
    if InfiniteVoid:
        print("Infinite Void (Void)")
        time.sleep(0.2)
    if item == "Sukuna":
        print("Cleave (Cleave)")
        time.sleep(0.2)
        print("Dismantle (Dismantle)")
        time.sleep(0.2)
        print("Malevolent Shrine (Shrine)")
        time.sleep(0.2)
        print("Fuga (Fuga)")
        time.sleep(0.2)
    if GalaxyImpact:
        print("Galaxy Impact (Galaxy)")
        time.sleep(0.2)
    if FishmanMartialArts:
        print("Fishman Martial Arts (Fishman)")
        time.sleep(0.2)
    if GangnumStyle:
        print("GangumStyle (Gangnum)")
        time.sleep(0.2)
    if Kamehameha:
        print("Kamehameha (Kame)")
        time.sleep(0.2)

    print("")

    UsedSpell = False
    MgcDamageSpell = False
    StrDamageSpell = False
    print(f"You have {Mana} mana.")
    time.sleep(0.5)
    Spell = input("Pick an available spell to use: ")
    print("")

    if Spell.lower() == "crit" and CritSpell:
        print("You selected the Crit Spell.")
        print("This spell makes your next attack a guaranteed critical hit.")
        trySpell = input("This spell costs 1 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if CritChance == 1:
                print("You already have max Crit Chance.")
            if Mana >= 1:
                Mana -= 1
                UsedSpell = True
                CritChance = 1

            else:
                print("You do not have enough mana.")

    elif Spell.lower() == "freeze" and FreezeSpell:
        print("You selected the Freeze Spell.")
        print("This spell freezes the enemy for 3 turns, lowering their defense and speed.")
        trySpell = input("This spell costs 2 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if EnemyFrozen:
                print("The enemy is already frozen.")
            elif Mana >= 2:
                Mana -= 2
                UsedSpell = True
                EnemyFrozen = True

                freezeTurn = Turn + 4
            else:
                print("You do not have enough mana.")

    elif Spell.lower() == "poison" and PoisonSpell:
        print("You selected the Poison Spell.")
        print("This spell poisons enemies for 3 to 5 turns, dealing 1 damage every turn.")
        trySpell = input("This spell costs 2 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if EnemyPoisoned:
                print("The enemy is already poisoned.")
            elif Mana >= 2:
                Mana -= 2
                UsedSpell = True
                EnemyPoisoned = True

                poisonTurn = Turn + 4
            else:
                print("You do not have enough mana.")

    elif Spell.lower() == "ichor" and IchorSpell:
        print("You selected the Ichor Spell.")
        print("This spell cuts enemy defense in half for 2 turns.")
        trySpell = input("This spell costs 3 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if EnemyIchored:
                print("The enemy is already inflicted with ichor.")
            elif Mana >= 3:
                Mana -= 3
                UsedSpell = True
                EnemyIchored = True
                ichorTurn = Turn + 3
            else:
                print("You do not have enough mana.")

    elif Spell.lower() == "explosion" and ExplosionSpell:
        print("You selected the Explosion Spell.")
        print("This spell ignores all enemy defense and deals one third of your Strength as damage.")
        trySpell = input("This spell costs 3 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Mana >= 3:
                Mana -= 3
                UsedSpell = True
                ExplosionsUsed += 1
                StrDamageSpell = True
                Damage = math.floor(Strength * 0.33)
            else:
                print("You do not have enough mana.")

    elif Spell.lower() == "purple" and HollowPurple:
        print("You selected the Hollow Purple Spell.")
        print(
            "This spell does your magic stat in damage with no defense reduction. \nYou also have to have infinity on.")
        if Ressurection:
            trySpell = input("This spell costs 0 mana in ressurection. Would you like to use it? (y): ")
        else:
            trySpell = input("This spell costs 30 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Ressurection:
                UsedSpell = True
                Damage = Magic
            else:
                if InfinityActivated:
                    if Mana >= 30:
                        Mana -= 30
                        UsedSpell = True
                        Damage = Magic
                    else:
                        print("You do not have enough mana.")
                else:
                    print("You do not have infinity.")

    elif Spell.lower() == "infinity" and Infinity:
        print(
            "You selected Infinity. \nInfinity doubles your defense for a turn and also allows the use of Gojo's other spells.")
        trySpell = input("This spell costs 30 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if not Ressurection:
                if InfinityActivated:
                    print("You already have infinity activated.")
                elif Mana >= 30:
                    InfinityActivated = True
                    Mana -= 30
                    UsedSpell = True
                    Defense *= 2
                else:
                    print("You do not have enough mana.")
            else:
                print("You cannot use infinity in ressurection.")
    elif Spell.lower() == "void" and InfiniteVoid:
        print("You selected Infinite Void.")
        print("This spell stuns the enemy for 2 turns.")
        trySpell = input("This spell costs 100 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Mana >= 100:
                Mana -= 100
                UsedSpell = True
                EnemyStunned = True
                stunTurn = Turn + 3
            else:
                print("You do not have enough mana.")

    elif Spell.lower() == "acid" and AcidSpell:
        print("You selected the Acid Spell.")
        print(
            "This spell deals 2 damage a turn and lasts for 3 turns. If you create acid by inflicting poison and ichor, it lasts for 5 turns.")
        trySpell = input("This spell costs 3 mana. Would you like to use it? (y): ")
        if EnemyAcidified:
            print("The enemy is already acidified.")
        elif Mana >= 3:
            Mana -= 3
            UsedSpell = True
            EnemyAcidified = True
            acidTurn = Turn + 4
        else:
            print("You do not have enough mana.")
    elif Spell.lower() == "heal" and HealOverTimeSpell:
        print("You selected the Heal Over Time Spell.")
        print("This spell heals you for 1.1x your max health every turn.")
        trySpell = input("This spell costs 3 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Mana >= 3:
                Mana -= 3
                UsedSpell = True
                playerHealing = True
                healTurn = Turn + 4
            else:
                print("You do not have enough mana.")
    elif Spell.lower() == "pray" and PraySpell:
        print("You selected pray.")
        print("God will decide your fate.")
        trySpell = input("This spell costs 5 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Mana >= 5:
                Mana -= 5
                UsedSpell = True
                effect = random.randint(1, 10)
                if effect == 1:
                    playerBurned = True
                    playerBurnTurn = Turn + 4
                    print("You have been burned.")
                elif effect == 2:
                    EnemyBurned = True
                    burnTurn = Turn + 4
                    print(f"The {Enemy} has been burned.")
                elif effect == 3:
                    Health += math.floor(maxHealth * 0.1)
                    if Health > maxHealth:
                        Health = maxHealth
                    print(f"You have been healed. You are now at {Health} health.")
                elif effect == 4:
                    Health = maxHealth
                    print("You are now at full health.")
                elif effect == 5:
                    Mana += math.floor(maxMana * 0.1)
                    if Mana > maxMana:
                        Mana = maxMana
                    print(f"Your mana has been restored. You now have {Mana} mana.")
                elif effect == 6:
                    Mana = maxMana
                    print("You now have max mana.")
                elif effect == 7:
                    print("The god was too lazy to do anything.")
                elif effect == 8:
                    if random.randint(1, 3) == 1:
                        stat = random.randint(1, 4)
                        if stat == 1:
                            Strength += math.floor(Strength * 0.1)
                            print(f"Your strength has been increased. It is now {Strength}.")
                        elif stat == 2:
                            Defense += math.floor(Defense * 0.1)
                            print(f"Your defense has been increased. It is now {Defense}.")
                        elif stat == 3:
                            Speed += math.floor(Speed * 0.1)
                            print(f"Your speed has been increased. It is now {Speed}.")
                        elif stat == 4:
                            Magic += math.floor(Magic * 0.1)
                            print(f"Your magic has been increased. It is now {Magic}.")
                    else:
                        print("The god smote you for fun.")
                        Health -= 1
                        print("Now you have {Health} health.")
                elif effect == 9:
                    print("Thoust opponent was smote.")
                    EnemyHealth -= 1 + (EnemyLevel * 0.3)
                elif effect == 10:
                    if random.randint(1, 2) == 1:
                        EnemyPoisoned = True
                        poisonTurn = Turn + 4
                        print(f"The {Enemy} was poisoned.")
                    else:
                        EnemyFrozen = True
                        freezeTurn = Turn + 4
                        print(f"The {Enemy} was frozen.")
            else:
                print("You do not have enough mana.")
    elif Spell.lower() == "cleave" and Cleave:
        print("You cleaved.")
        Damage = (Strength + Magic) - EnemyDefense
        UsedSpell = True
        StrDamageSpell = True
    elif Spell.lower() == "dismantle" and Dismantle:
        print("You dismantled.")
        Damage = math.floor(Strength * 1.5)
        UsedSpell = True
        StrDamageSpell = True
    elif Spell.lower() == "shrine" and MalevolentShrine:
        print("You opened your domain.")
        if Mana >= 40:
            Mana -= 40
            MgcDamageSpell = True
            UsedSpell = True
            Damage = Magic
        else:
            print("Nevermind you have NO mana.")
    elif Spell.lower() == "fuga" and Fuga:
        if item == "Sukuna":
            print("You used a fire arrow.")
            if Mana >= 20:
                Mana -= 20
                UsedSpell = True
                MgcDamageSpell = True
                Damage = math.floor(Magic * 0.9)
                burnTurn = Turn + 5
                EnemyBurned = True
            else:
                print("You do not have enough mana.")
        else:
            print("You selected Fuga.")
            print("This spell deals 50% of your magic and ignores all enemy defense. It also burns the enemy.")
            trySpell = input("This spell costs 10 mana. Would you like to use it? (y): ")
            if trySpell == "y":
                if Mana >= 10:
                    Mana -= 10
                    UsedSpell = True
                    MgcDamageSpell = True
                    Damage = math.floor(Magic * 0.5)
                    burnTurn = Turn + 5
                    EnemyBurned = True
                else:
                    print("You do not have enough mana.")
    elif Spell.lower() == "galaxy" and GalaxyImpact:
        trySpell = input("This spell costs 5 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Mana >= 5:
                Mana -= 5
                UsedSpell = True
                MgcDamageSpell = True
                print("You dropped a Nuke.")
                Damage = (Strength + Magic)
            else:
                print("You do not have enough mana.")
    elif Spell.lower() == "fishman" and FishmanMartialArts:
        print("You used the Fishman Martial Arts.")
        Damage = Strength - EnemyDefense + 2
        StrDamageSpell = True
        UsedSpell = True
    elif Spell.lower() == "gangnum" and GangnumStyle:
        trySpell = input("This spell costs 200 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Mana >= 200:
                Mana -= 200
                UsedSpell = True
                MgcDamageSpell = True
                print("You used Gangum Style.")
                Damage = (Strength + Magic) * 3
        else:
            print("That is not a valid spell.")
    elif Spell.lower() == "kame" and Kamehameha:
        trySpell = input("This spell costs 1 mana. Would you like to use it? (y): ")
        if trySpell == "y":
            if Mana >= 1:
                Mana -= 1
                UsedSpell = True
                MgcDamageSpell = True
                print("You used Kame.")
                Damage = (Strength + Magic)
    if UsedSpell:
        print(f"Your {Spell.lower()} spell was successful. You now have {Mana} mana.")
        if MgcDamageSpell:
            doAttack(Damage, EnemyDamage, "mgc")
        elif StrDamageSpell:
            doAttack(Damage, EnemyDamage, "str")
        else:
            enemyAttacks(EnemyDamage)


def statuses():
    global EnemyFrozen, EnemyBurned, EnemyPoisoned, EnemyIchored, EnemyAcidified, EnemyStunned
    global Turn, burnTurn, poisonTurn, ichorTurn, freezeTurn, acidTurn, stunTurn
    global playerHealing, healTurn, playerBurned, playerBurnTurn
    global EnemyHealth, EnemyDefense, EnemySpeed, EnemyDamage
    global Health, maxHealth

    if EnemyBurned:
        if burnTurn is not None and burnTurn == Turn:
            EnemyBurned = False
            burnTurn = None
            print(f"The {Enemy} is no longer burned.")
        else:
            if EnemyFrozen:
                EnemyBurned = False
                burnTurn = None
                print(f"You canceled the {Enemy}'s burning.")
                EnemyHealth -= 3
                print(f"They took 3 damage from the burn cancel. It is now at {EnemyHealth} health.")
            else:
                EnemyHealth -= 2
                print(f"The {Enemy} is burning. They are now on {EnemyHealth} health.")

    if EnemyPoisoned:
        if poisonTurn is not None and poisonTurn == Turn:
            EnemyPoisoned = False
            poisonTurn = None
            print(f"The {Enemy}'s poison wore off.")
        else:
            if EnemyIchored and not EnemyAcidified:
                EnemyPoisoned = False
                EnemyIchored = False
                print(f"You created acid by combining ichor and poison.")
                EnemyAcidified = True
                global acidSpellUnlocked
                acidSpellUnlocked = True
                acidTurn = Turn + 5
                poisonTurn = None
                ichorTurn = None
            else:
                EnemyHealth -= 1
            print(f"The {Enemy} is inflicted with poison.")
            print(f"They took 1 damamge. They are now at {EnemyHealth} health.")

    if EnemyIchored:
        defenseChange = 0
        if ichorTurn is not None and ichorTurn == Turn:
            EnemyIchored = False
            EnemyDefense += defenseChange
            ichorTurn = None
            print(f"The {Enemy}'s ichor wore off.")
        else:
            print(f"The {Enemy} is inflicted with ichor.")
            if ichorTurn == Turn - 1:
                defenseChange = round(EnemyDefense * 0.5)
                EnemyDefense -= defenseChange

    if EnemyFrozen:
        statChange = 0
        if freezeTurn is not None and freezeTurn == Turn:
            EnemyFrozen = False
            freezeTurn = None
            EnemySpeed += statChange
            EnemyDefense += statChange
            print(f"The {Enemy} unfroze.")
            print(f"Enemies defense is {EnemyDefense}")
        else:
            print(f"The {Enemy} is frozen.")
            if freezeTurn == Turn + 2:
                statChange = round(EnemySpeed / 1.5)
                EnemySpeed -= statChange
                EnemyDefense -= statChange
    if EnemyAcidified:
        if acidTurn is not None and acidTurn == Turn:
            EnemyAcidified = False
            acidTurn = None
            print(f"The {Enemy}'s acid wore off.")
        else:
            EnemyHealth -= 2
            print(f"The {Enemy} is inflicted with acid.")
    if EnemyStunned:
        if stunTurn is not None and stunTurn == Turn:
            EnemyStunned = False
            stunTurn = None
            print(f"The {Enemy} is no longer stunned.")
        else:
            EnemyDamage = 0
            print(f"The {Enemy} is stunned.")
    if EnemyFrozen or EnemyBurned or EnemyIchored or EnemyPoisoned or EnemyAcidified or EnemyStunned:
        print("")
    if playerHealing:
        if healTurn is not None and healTurn == Turn:
            playerHealing = False
            healTurn = None
            print("You stopped healing.")
        else:
            if math.floor(maxHealth * 0.15) >= 1:
                Health += math.floor(maxHealth * 0.1)
            else:
                Health += 1
            print(f"You have a healing effect and are now at {Health} health.")
    if playerBurned:
        if playerBurnTurn is not None and playerBurnTurn == Turn:
            playerBurned = False
            playerBurnTurn = None
            print(f"You are no longer burned.")
        else:
            Health -= 2


def startTurn():
    global item, weapon, Strength, Magic, Defense, Speed, Health, XP
    global nextLevel, Level, EnemyDamage, EnemiesLeft, CritChance, EnemyAccuracy
    if Enemy != "Giant Enemy Spider" and Enemy != "Spider" and Enemy != "Flamingo":
        if EnemyStrength > EnemyMagic:
            EnemyDamage = EnemyStrength - Defense if EnemyStrength > Defense else 1
            print(f"The {Enemy} intends to attack with its strength.")
        else:
            EnemyDamage = EnemyMagic - math.floor(Defense / 2)
            if EnemyDamage <= 1:
                EnemyDamage = 1
            print(f"The {Enemy} intends to attack with its magic.")

    elif Enemy == "Spider":
        if (EnemySpeed / 2) >= Defense:
            print(f"The {Enemy} intends to attack with its speed.")
            EnemyDamage = (EnemySpeed * 2) - Defense
        else:
            EnemyDamage = 1

    elif Enemy == "Giant Enemy Spider":
        chance = random.randint(1, 3)
        if chance == 1:
            EnemyAccuracy = 0.8
            EnemyDamage = EnemyStrength - Defense if EnemyStrength > Defense else 1
            print(f"The {Enemy} intends to attack with its strength.")
        elif chance == 2:
            EnemyAccuracy = 0.8
            EnemyDamage = EnemyMagic - math.floor(Defense / 2)
            if EnemyDamage <= 1:
                EnemyDamage = 1
            if EnemyDamage > EnemyMagic:
                EnemyDamage = EnemyMagic
            print(f"The {Enemy} intends to attack with its magic.")
        elif chance == 3:
            EnemyAccuracy = 1
            if (EnemySpeed / 2) >= Defense:
                print(f"The {Enemy} intends to attack with its speed.")
                EnemyDamage = (EnemySpeed * 2) - Defense
            else:
                EnemyDamage = 0
    elif Enemy == "Flamingo":
        chance = random.randint(1, 3)
        if chance == 1:
            EnemyAccuracy = 0.8
            EnemyDamage = EnemyStrength - Defense if EnemyStrength > Defense else 1
            print(f"The {Enemy} intends to attack with its strength.")
        elif chance == 2:
            EnemyAccuracy = 0.8
            EnemyDamage = EnemyMagic - math.floor(Defense / 2)
            if EnemyDamage <= 1:
                EnemyDamage = 1
            print(f"The {Enemy} intends to attack with its magic.")
        elif chance == 3:
            EnemyAccuracy = 0.9
            print(f"The {Enemy} intends to attack with its magic and strength.")
            EnemyDamage = ((EnemyMagic / 2) + EnemyStrength) - Defense
        if EnemyDamage <= 1:
            EnemyDamage = 1
    time.sleep(0.5)
    Action = input("What action do you wish to perform? (atk/spell/other): ")
    if Action.lower() == "atk":
        if Speed > (Strength * 2) or Speed > (Magic * 2):
            AttackType = input("Woud you like to use strength, magic, or speed? (Str/Mgc/Spd): ")
        else:
            AttackType = input("Would you like to use strength or magic? (Str/Mgc): ")
        print("")
        if AttackType.lower() == "str":
            Damage = Strength - EnemyDefense if Strength > EnemyDefense else 1
            if Damage > Strength:
                Damage = Strength
            doAttack(Damage, EnemyDamage, AttackType.lower())
        elif AttackType.lower() == "mgc":
            Damage = Magic - EnemyDefense // 2 if Magic > EnemyDefense // 2 else 1
            if Damage > Magic:
                Damage = Magic
            critChance = random.random()
            doAttack(Damage, EnemyDamage, AttackType.lower())
        elif AttackType.lower() == "spd" and (Speed > (Strength * 2) or Speed > (Magic * 2)):
            if (Speed / 2) > EnemyDefense:
                Damage = (Speed * 2) - EnemyDefense
            else:
                Damage = 0
            doAttack(Damage, EnemyDamage, AttackType.lower())

    elif Action.lower() == "spell":
        if Magic < 3:
            print("You don't have enough magic, you don't know any spells.")
        else:
            useSpell()
    elif Action.lower() == "other":
        Action = input("What would you like to do? (item/run/wait/info): ")
        if Action.lower() == "item":
            if item is None:
                print("You have no item.")
            elif item == "Potion":
                usepot = input(f"You have a {potion} potion. Would you like to use it? (y): ")
                if usepot == "y":
                    apply_potion_effects(potion)
            elif item == "Weapon":
                useItem = input(
                    f"Your {weapon.lower()} enhancing weapon is equipped by default. Would you like to get rid of it? (y): ")
                if useItem == "y":
                    adjust_weapon_stats(False)
                    weapon = None
                    item = None
                    print("You have lost your weapon.")
            elif item == "Phoenix Feather":
                print("You have a phoenix feather.")
                print("This item has a passive that, when you die, you respawn at half health.")
                print("It is a one time use item.")
                useItem = input("Would you like to throw it away? (y): ")
                if useItem == "y":
                    item = None
            elif item == "Money Bag":
                print("You have a money bag.")
                print(
                    "When you use it, you gain some money. The amount of money you recieve is usually around a few cents.")
                useItem = input("Would you like to use it? (y): ")
                if useItem.lower() == "y":
                    global money, maxMoney
                    money += (random.randint(2, 4) / 100)
                    if money > maxMoney:
                        money = maxMoney
                    item = None
            elif item == "Flamingo Wings":
                print("You have some flamingo wings.")
                print("When you use it, you gain some max hp perminently.")
                useItem = input("Would you like to use it? (y): ")
                if useItem.lower() == "y":
                    global maxHealth
                    HealthIncrease = random.randint(2, 4) + Level
                    maxHealth += HealthIncrease
                    Health += HealthIncrease
                    print(f"You now have {maxHealth} max health.")
            else:
                print(f"You have a {item}.")
        elif Action.lower() == "info":
            infowho = input("Who would you like to see the stats of? (Enemy/You) ")
            if infowho.lower() == "you":
                print("Your stats are:")
                time.sleep(0.4)
                print(f"speed: {Speed}")
                time.sleep(0.4)
                print(f"strength: {Strength}")
                time.sleep(0.4)
                print(f"defense: {Defense}")
                time.sleep(0.4)
                print(f"magic: {Magic}")
                time.sleep(0.4)
                print(f"health: {Health}")
                time.sleep(0.4)
                if money > 0.01:
                    print(f"You have {money} cents.")
                elif money == 0.01:
                    print("You have 0.01 cent.")
                else:
                    print("You have no money.")
                if nextLevel > XP:
                    print(f"Your XP is {XP} and you need {nextLevel - XP} XP to level up.")
                else:
                    print(f"You have {XP} XP. You have more XP than the next level up.")
                time.sleep(0.4)
                print(f"Your current level is {Level}.")
                time.sleep(0.4)
                if item != None:
                    if item == "Potion":
                        print(f"Your item is a {potion.lower()} potion.")
                    elif item == "Weapon":
                        print(f"Your item is a {weapon.lower()} enhancing weapon.")
                    else:
                        print(f"Your item is a {item}.")
                else:
                    print("You have no item.")
            elif infowho.lower() == "enemy":
                print(f"The {Enemy}'s stats are:")
                time.sleep(0.4)
                print(f"speed: {EnemySpeed}")
                time.sleep(0.4)
                print(f"strength: {EnemyStrength}")
                time.sleep(0.4)
                print(f"defense: {EnemyDefense}")
                time.sleep(0.4)
                print(f"magic: {EnemyMagic}")
                time.sleep(0.4)
                print(f"health: {EnemyHealth}")
                time.sleep(0.4)
        elif Action.lower() == "wait":
            print("Waiting generates mana back.")
            global Mana
            print("You chose to wait.")
            Mana += math.floor(maxMana * 0.1)
            if Mana > maxMana:
                Mana = maxMana
            print(f"You now have {Mana} mana.")
            enemyAttacks(EnemyDamage)
        elif Action.lower() == "run":
            global EnemyLevel, runChance
            Run = input(f"Would you like to run away? {math.floor(runChance * 100)}% chance to successfully run. (y): ")
            if Run == "y":
                running = random.random()
                if running <= runChance:
                    print("You successfully ran away.")
                    EnemiesLeft += 1
                    EnemyLevel += 1
                    return True
                else:
                    print("You failed running. The enemy gets to attack now.")
                    if runChance < 0.8:
                        runChance += round(random.uniform(0.05, 0.15), 2)
                    else:
                        runChance = 0.8
                    enemyAttacks(EnemyDamage)
        return False


def battleEnd():
    global Health, XP, startHealth, item, weapon, nextLevel, Level, EnemyLevel, money, maxMoney
    global EnemyFrozen, EnemyBurned, EnemyPoisoned, EnemyIchored, Turn, EnemyAcidified, EnemyStunned
    print(f"You killed the {Enemy}!")
    EnemyPoisoned = False
    EnemyFrozen = False
    EnemyIchored = False
    EnemyBurned = False
    EnemyAcidified = False
    EnemyStunned = False
    EnemyLevel += 1
    DamageTaken = max(0, startHealth - Health)
    BaseXP = max(0, (DamageTaken * 2) - (DamageTaken // 2))
    XP_Gained = BaseXP + Turn + math.floor(EnemyLevel / 2)
    MoneyGained = 0.02 if item == "Lucky Coin" else 0.01
    Turn = 0
    if not money + MoneyGained >= maxMoney:
        money += MoneyGained
    else:
        money = maxMoney
    if MoneyGained == 0.01:
        print(f"You recieved {MoneyGained} cent. You now have {round(money, 2)} cents.")
    else:
        print(f"You recieved {MoneyGained} cents. You now have {round(money, 2)} cents.")
    XP += XP_Gained
    time.sleep(0.5)
    print(f"You took {DamageTaken} damage and received {XP_Gained} XP.")
    XPcheck()
    time.sleep(0.4)
    print(f"You now have {XP} XP.")
    time.sleep(1)
    print(f"Next Level up is in {nextLevel - XP} more XP.")
    time.sleep(0.4)
    print(f"Your current level is {Level}.")
    time.sleep(1)

    healChance = random.randint(1, 10)
    healed = 0
    if healChance <= 6:
        healed = math.floor(maxHealth * 0.2)
        Health += healed
    elif healChance <= 9:
        healed = math.floor(maxHealth * 0.4)
        Health += healed
    elif healChance == 10:
        healed = math.floor(maxHealth * 0.6)
        Health += healed

    if Health > maxHealth:
        Health = maxHealth
    print(f"You healed {healed} hp at the end of combat. You are now at {Health} health.")
    startHealth = Health
    time.sleep(1)
    if Enemy == "Mimic":
        if EnemyLevel > 10:
            itemGive(3)
        else:
            itemGive(2)
    elif Enemy == "Flamingo":
        global potion
        print("The flamingo boss dropped some flamingo wings.")
        if item != None:
            if item == "Potion":
                print(f"You already have a {potion} potion.")
            elif item == "Weapon":
                print(f"You already have a {weapon} enhancing weapon.")
            else:
                print(f"You already have a {item}.")
        flamingopickup = input("Would you like to pick up the flamingo wings? (y): ")
        if flamingopickup.lower() == "y":
            if item == "Weapon":
                adjust_weapon_stats(False)
                weapon = None
            elif item == "Potion":
                potion = None
            item = "Flamingo Wings"
    else:
        itemChance = random.randint(1, 10)
        if itemChance == 1:
            if EnemyLevel >= 10:
                itemGive(2)
            else:
                itemGive(1)


def setupPlayer():
    global Speed, Strength, Defense, Magic, Health, maxHealth, Accuracy, Mana, maxMana
    Speed = 6
    Strength = 6
    Defense = 6
    Magic = 5
    maxMana = 5 + random.randint(2, 3)
    Mana = maxMana
    Health = 5
    maxHealth = 5
    Accuracy = 0.8
    print("Your stats are:")
    time.sleep(0.5)
    print(f"Health: {Health}")
    time.sleep(0.5)
    print(f"Speed: {Speed}")
    time.sleep(0.5)
    print(f"Strength: {Strength}")
    time.sleep(0.5)
    print(f"Defense: {Defense}")
    time.sleep(0.5)
    print(f"Magic: {Magic}")
    time.sleep(0.5)


def die():
    global gotDeathBlowed, EnemiesLeft, EnemiesKilled, itemsCollected
    global maxHealth, Speed, Strength, Defense, Magic, XP, Level
    time.sleep(1)
    if gotDeathBlowed:
        print("Oh ouch that hurts. Dying to a death blow must suck.")
    else:
        print("Dang, you died. Better luck next time.")
    time.sleep(0.5)
    print("")
    print("Stats:")
    time.sleep(0.5)
    print(f"Max Health: {maxHealth}")
    time.sleep(0.5)
    print(f"Speed: {Speed}")
    time.sleep(0.5)
    print(f"Strength: {Strength}")
    time.sleep(0.5)
    print(f"Defense: {Defense}")
    time.sleep(0.5)
    print(f"Magic: {Magic}")
    time.sleep(0.5)
    print(f"Max Mana: {maxMana}")
    time.sleep(0.5)
    print(f"Enemies encountered: {EnemiesKilled + EnemiesLeft + (1 if gotDeathBlowed == False else 0)}")
    time.sleep(0.5)
    print(f"Enemies killed: {EnemiesKilled}")
    time.sleep(0.5)
    print(f"Enimies left alone: {EnemiesLeft}")
    time.sleep(0.5)
    print(f"Items collected: {itemsCollected}")
    time.sleep(0.5)
    print(f"XP: {XP}")
    time.sleep(0.5)
    print(f"Level: {Level}")


def gameLoop():
    global Health, EnemyHealth, EnemyStrength, EnemyDefense, EnemyMagic, EnemySpeed, startHealth, Speed, Strength, Defense, Magic, EnemiesKilled, EnemiesLeft, itemsCollected, XP, Level, EnemyLevel, Turn, floorLevel, Enemy, item, potion, weapon, FoughtGiantSpider, maxHealth, Ressurection
    print("")
    startHealth = Health
    EnemyHealth = 1
    floorLevel += 1
    room = 1
    if floorLevel == 0:
        EnemyCheck()
    elif floorLevel >= 20 and EnemyLevel == 20:
        Enemy = "Giant Enemy Spider"
        print("You have encountered a boss, the Giant Enemy Spider!.")
        time.sleep(0.5)
        EnemySpeed = Speed + 10
        EnemyStrength = 45
        EnemyDefense = 30
        EnemyMagic = 25
        EnemyAccuracy = 0.85
        EnemyHealth = 40
    elif floorLevel >= 40 and EnemyLevel == 40:
        Enemy = "Flamingo"
        print("You have encountered a boss, the Flamingo!.")
        time.sleep(0.5)
        EnemySpeed = 65 + random.randint(5, 10)
        EnemyStrength = 40 + random.randint(5, 10)
        EnemyDefense = 50 + random.randint(5, 10)
        EnemyMagic = 60 + random.randint(5, 10)
        EnemyAccuracy = 0.9
        EnemyHealth = 60
    else:
        if random.randint(1, 10) == 1:
            oldRoom = room
            while True:
                room = random.randint(1, 9)
                if room != oldRoom:
                    break
            if room != 6:
                Enemy = False
            if room == 1:
                treasure = input(
                    "You enter a room. There looks to be some treasure in the middle of the room. Do you want to take it? (y): ")
                if treasure.lower() == "y":
                    if random.randint(1, 4) == 1:
                        print("Oh, that wasn't treasure.")
                        EnemyCheck()
                    else:
                        Enemy = False
                        print("You found some treasure!")
                        if random.randint(1, 6) <= 5:
                            print("It was uncommon loot.")
                            itemGive(2)
                        else:
                            print("It was rare loot!")
                            itemGive(3)
            elif room == 2:
                EnemyCheck()
            elif room == 3:
                treasure = input("You found some treasure. Take it? (y): ")
                if treasure.lower() == "y":
                    if random.randint(1, 5) <= 3:
                        print("It was some common loot.")
                        itemGive(1)
                    else:
                        print("It was uncommon loot.")
                        itemGive(2)
            elif room == 4:
                global money, praySpellUnlocked
                print("You found a shop!")
                time.sleep(0.2)
                if money > 0.01 and money < 1:
                    print(f"You have {money} cents.\n")
                elif money == 0.01:
                    print(f"You have {money} cent.\n")
                elif money == 1:
                    print(f"You have {money} dollar.\n")
                time.sleep(0.5)
                ShopShenanigans = [
                    {"name": "Strength Potion", "effect": "Strength increase by 10% permanently.", "cost": 0.01},
                    {"name": "Defense Potion", "effect": "Defense increase by 10% permanently.", "cost": 0.01},
                    {"name": "Speed Potion", "effect": "Speed increase by 10% permanently.", "cost": 0.01},
                    {"name": "Magic Potion", "effect": "Magic increase by 10% permanently.", "cost": 0.01},
                    {"name": "Health Potion", "effect": "Heal to full health.", "cost": 0.01},
                    {"name": "Mana Potion", "effect": "Restore Mana to Max", "cost": 0.01},
                    {"name": "Lucky Coin", "effect": "Increases money per kill.", "cost": 0.03},
                    {"name": "Prayer Spell", "effect": "Pray to god and hope you get a good effect.", "cost": 0.05}
                ]
                openedShop = False
                while True:
                    if not openedShop:
                        shop_items_to_print = random.sample(ShopShenanigans, 3)
                        for Thingy in shop_items_to_print:
                            if Thingy['name'] == "Lucky Coin" and random.randint(1, 2) == 1:
                                break
                            print(f"Item: {Thingy['name']}")
                            time.sleep(0.5)
                            print(f"Effect: {Thingy['effect']}")
                            time.sleep(0.5)
                            print(f"Cost: {Thingy['cost']}")
                            time.sleep(0.5)
                            print("")
                            openedShop = True
                    buy = input("\nWhat would you like to buy? (Item name/leave): ")
                    if buy.lower() == "leave":
                        break
                    for shop_item in shop_items_to_print:
                        if buy == shop_item['name'] or shop_item['name'].lower():
                            replaceItem = "y"
                            if item != None and shop_item['name'] != "Prayer Spell":
                                print(f"You already have an item. You have a {item}.")
                                if item == "Potion":
                                    print(f"It is a {potion.lower()} potion.")
                                elif item == "Weapon":
                                    print(f"It is a {weapon.lower()} enhancing weapon.")
                                replaceItem = input(f"Would you like to replace it with {shop_item['name']}? (y): ")
                            if replaceItem.lower() == "y":
                                if money >= shop_item['cost']:
                                    print(f"sucessfully bought {shop_item['name']}.\n")
                                    money -= shop_item['cost']
                                    if shop_item['name'] == "Strength Potion":
                                        item = "Potion"
                                        potion = "Strength"
                                        weapon = None
                                    elif shop_item['name'] == "Defense Potion":
                                        item = "Potion"
                                        potion = "Defense"
                                        weapon = None
                                    elif shop_item['name'] == "Speed Potion":
                                        item = "Potion"
                                        potion = "Speed"
                                        weapon = None
                                    elif shop_item['name'] == "Magic Potion":
                                        item = "Potion"
                                        potion = "Magic"
                                        weapon = None
                                    elif shop_item['name'] == "Health Potion":
                                        item = "Potion"
                                        potion = "Health"
                                        weapon = None
                                    elif shop_item['name'] == "Mana Potion":
                                        item = "Potion"
                                        potion = "Mana"
                                        weapon = None
                                    elif shop_item['name'] == "Lucky Coin":
                                        item = "Lucky Coin"
                                        potion = None
                                        weapon = None
                                    elif shop_item['name'] == "Prayer Spell":
                                        praySpellUnlocked = True
                                    break
                                else:
                                    print(f"You don't have enough money to buy {shop_item['name']}.\n")
                                    break
                            else:
                                print("You cannot buy that.\n")
                                break
                    if money == 0:
                        print("Toji ahh")
                        break
            elif room == 5:
                print(
                    "You found a room with 3 chests in it. There's a sign on the wall that warns you about danger in the area.")
                chestTechnique = input("Which chest would you like top open? (1/2/3): ")
                mimicChest = random.randint(1, 3)
                if chestTechnique == "1":
                    if mimicChest == 1:
                        print("Wrong chest! You found a mimic.")
                        Enemy = "Mimic"
                        EnemySpeed = random.randint(1, 3) + EnemyLevel
                        EnemyStrength = random.randint(4, 7) + EnemyLevel
                        EnemyDefense = random.randint(5, 7) + EnemyLevel
                        EnemyMagic = random.randint(1, 4) + EnemyLevel
                        EnemyAccuracy = 0.75
                        EnemyHealth = 8 + EnemyLevel
                    else:
                        print("You picked a good chest! You found some loot.")
                        itemGive(2)
                elif chestTechnique == "2":
                    if mimicChest == 2:
                        print("Wrong chest! You found a mimic.")
                        Enemy = "Mimic"
                        EnemySpeed = random.randint(1, 3) + EnemyLevel
                        EnemyStrength = random.randint(4, 7) + EnemyLevel
                        EnemyDefense = random.randint(5, 7) + EnemyLevel
                        EnemyMagic = random.randint(1, 4) + EnemyLevel
                        EnemyAccuracy = 0.75
                        EnemyHealth = 8 + EnemyLevel
                    else:
                        print("You picked a good chest! You found some loot.")
                        itemGive(2)
                elif chestTechnique == "3":
                    if mimicChest == 3:
                        print("Wrong chest! You found a mimic.")
                        Enemy = "Mimic"
                        EnemySpeed = random.randint(1, 3) + EnemyLevel
                        EnemyStrength = random.randint(4, 7) + EnemyLevel
                        EnemyDefense = random.randint(5, 7) + EnemyLevel
                        EnemyMagic = random.randint(1, 4) + EnemyLevel
                        EnemyAccuracy = 0.75
                        EnemyHealth = 8 + EnemyLevel
                    else:
                        print("You picked a good chest! You found some loot.")
                        itemGive(2)
                else:
                    print("You didnt pick a chest.")
            elif room == 6:
                if Enemy:
                    if Enemy == "Skeleton":
                        print("But it refused.")
                        EnemyHealth = (3 + EnemyLevel) * 2
                        EnemyMagic = round(EnemyMagic + (EnemyStrength * 0.67))
                        EnemyStrength = 0
                        EnemyDefense = math.ceil(EnemyDefense / 3)
                    elif Enemy == "Toji":
                        print(
                            "*You notice someone on top of a building talking to what looks to be some random old lady*")
                        time.sleep(1)
                        print("")
                        EnemyHealth = math.floor((3 + EnemyLevel) * 1.1)
                        EnemySpeed = math.floor(EnemySpeed * 1.2)
                        EnemyStrength = math.floor(EnemyStrength * 1.2)
                        EnemyDefense = math.ceil(EnemyDefense * 0.8)
                    else:
                        time.sleep(0.5)
                        print("There's an enemy standing at the end of the room. This enemy looks familiar...")
                        time.sleep(1)
                        print(f"Oh, that {Enemy} you just killed is back for more.")
                        time.sleep(0.5)
                        print("")
                        EnemyHealth = (3 + EnemyLevel) * 2
                        EnemyStrength *= 2
                        EnemyDefense = math.ceil(EnemyDefense / 3)
                else:
                    EnemyCheck()
            elif room == 7:
                print("There's a rather strong looking enemy guarding some loot in this room.")
                fight = input("The loot looks good, do you want to fight the enemy for the loot? (y): ")
                if fight == "y":
                    EnemyCheck()
                    EnemyDefense = round(EnemyDefense * 1.5)
                    EnemySpeed = round(EnemySpeed * 1.5)
                    EnemyMagic = round(EnemyMagic * 1.5)
                    EnemyStrength = round(EnemyStrength * 1.5)
            elif room == 8:
                print("There's a fountain sitting in the middle of the room.")
                print("There's a sign that says its a healing fountain, and it costs 0.01 cent to use.")
                print(f"You have {money} cents and {Health} health.")
                fountain = input("Do you want to toss a coin in the fountain? (y): ")
                if fountain == "y" and money >= 0.01:
                    money -= 0.01
                    Health += math.ceil(maxHealth / 2)
                    if Health > maxHealth:
                        Health = maxHealth
                    print(f"The fountain healed you. You now have {Health} health.")
                elif money < 0.01:
                    print("You don't have enough money to use the fountain.")
                    if Health < math.floor(maxHealth / 3) and random.randint(1, 2) == 1:
                        print("Luckily, someone left a coin laying around and you were able to use it.")
                        Health += math.ceil(maxHealth / 2)
                        if Health > maxHealth:
                            Health = maxHealth

            elif room == 9:
                Enemy = "Toji"
                EnemySpeed = random.randint(1, 3) + (EnemyLevel * 3)
                EnemyStrength = random.randint(1, 1) + (EnemyLevel * 3)
                EnemyDefense = 1 + EnemyLevel
                EnemyMagic = 0
                EnemyAccuracy = 0.95
                EnemyHealth = 6 + EnemyLevel
                print("You found Toji. Uh oh!")
                if Ressurection:
                    print("You are in ressurection. You win!\n\n")
                    EnemyHealth = 0
                    print("Toji: Somethings off.")
                    time.sleep(1)
                    print(
                        "Toji: I refuse to do any work for free. Normally I would have said that and hightailed it out of there. Yet the freshly awakened yeilder of the limitless technique was right before my eyes.")
                    time.sleep(3)
                    print(
                        "Toji: He was probably the strongest jujutsu sorcerer of the modern age. I wanted to reject him. I wanted to bring him to his knees. I wanted to take down the pinnicle of the jujutsu world in the Zenin clan that rejected me.")
                    time.sleep(4)
                    print(
                        "Toji: I twisted myself into knots for so long. All to try justifying my life. That was the moment I truly lost.")
                    time.sleep(3)
                    print("*chain falling* *grabs what would have been his side*")
                    time.sleep(2)
                    print(
                        "Toji: I thought you had abandoned that pride. I thought you had chosen to live without respecting yourself, or anyone else for that matter.")
                    time.sleep(5)
                    print("You: Do you have any last words to say?")
                    time.sleep(1.8)
                    print("Toji: Not really.")
                    time.sleep(1.5)
                    print("*Megumi flashbacks*")
                    time.sleep(3)
                    print(
                        "Toji: Two or three years from now, my kid will be sold to the Zenin clan. Do what you will with that.")
                    time.sleep(1)
                    print("*Looks down and dies peacefully*")
                    time.sleep(7)
                    print("\n\n")
            elif room == 10:
                pass
        else:
            EnemyCheck()
    if Enemy:
        global runChance
        runChance = 0.5
        while Health > 0 and EnemyHealth > 0:
            Turn += 1
            ran = startTurn()
            print("")
            if ran:
                break
        if Health == 0:
            if item == "Phoenix Feather":
                Health = math.ceil(maxHealth / 2)
                item = None
                print("You have used your Phoenix Feather and have been healed to half health.")
                while Health > 0 and EnemyHealth > 0:
                    Turn += 1
                    ran = startTurn()
                    print("")
                    if ran:
                        break
                if Health == 0:
                    die()
                elif EnemyHealth == 0:
                    battleEnd()
                    print("")
                    time.sleep(0.5)
            elif item == "Weapon":
                if weapon == "Cursed Energy" and not Ressurection:
                    Health = math.ceil(maxHealth / 2)
                    maxHealth = math.ceil(maxHealth * 0.67)
                    Defense = math.floor(Defense / 2)
                    Strength = math.floor(Strength * 2)
                    Speed = math.floor(Speed * 2)
                    Magic = math.floor(Magic * 2)
                    print("You: Hey there. It's been a while, huh?")
                    time.sleep(1.5)
                    print(f"{Enemy}: Are you for real?")
                    time.sleep(1)
                    print("You: I'm for real real. I'm still alive and kickin'!")
                    time.sleep(2.5)
                    print(f"{Enemy}: Reverse cursed technique.")
                    time.sleep(1)
                    print(
                        "You: Exactly. When you hit me I gave up counter attacking and poured all my focus into the reverse cursed technique. Cursed energy is negative energy, and while it can enhance the body it can't regenerate it. So you can multiply that energy against itself to create positive energy! That's the reverse cursed technique! It's easier said than done, I could never do it until now!")
                    time.sleep(10)
                    print(f"{Enemy}: Somethings off, he's blabbing on. Is he high?")
                    time.sleep(2.5)
                    print(
                        "You: But I finally grasped it on the verge of death. The true essence of cursed energy! The reason you're going to lose is because you didn't chop my head off! And because you didn't use that cursed tool when you stabbed me in the head!")
                    time.sleep(7)
                    print(f"{Enemy}: I'm gonna lose?")
                    time.sleep(1)
                    print(f"{Enemy}: Our fight is just getting started.")
                    time.sleep(1.5)
                    print("You: Is that right? You could be right. YOU'RE SO RIGHT!")
                    time.sleep(3)
                    print("\nYou got an increase in most stats.")
                    Ressurection = True

                    while Health > 0 and EnemyHealth > 0:
                        Turn += 1
                        ran = startTurn()
                        print("")
                        if ran:
                            break
                    if Health == 0:
                        die()
                    elif EnemyHealth == 0:
                        battleEnd()
                        print("")
                        time.sleep(0.5)
            else:
                die()
        elif EnemyHealth == 0:
            battleEnd()
            if room == 7:
                itemGive(3)
            print("")
            time.sleep(0.5)


if AnimeSpecs.lower() == "y":
    AnimeSpecs = True
else:
    AnimeSpecs = False

if Start == "":
    setupPlayer()
    while Health > 0:
        gameLoop()
elif Start == "kyle fr":
    Strength = 7
    Defense = 7
    Speed = 7
    Magic = 6
    Accuracy = 0.95
    CritChance = 0.3
    Health = 6
    maxHealth = 6
    maxMana = Magic + random.randint(3, 4)
    Mana = maxMana
    praySpellUnlocked = True
    item = "Phoenix Feather"
    print("Your stats are:")
    time.sleep(0.5)
    print(f"Health: {Health}")
    time.sleep(0.5)
    print(f"Speed: {Speed}")
    time.sleep(0.5)
    print(f"Strength: {Strength}")
    time.sleep(0.5)
    print(f"Defense: {Defense}")
    time.sleep(0.5)
    print(f"Magic: {Magic}")
    time.sleep(0.5)
    print("")
    while Health > 0:
        gameLoop()
elif Start == "er;aimeroijqerojrovrwjpqwojfewpo theres no point dont try this code gjoaigjeaoij epoaewfoeijpaj if you copy it youre gaya qiogjogwij qwogijweowfjeoij and if you change it your also gay auewgoqogijqofwijewofjewoewoejfeio dont use this code jioagaeriojioeaw id delete it but im too lazy and i feel like it could have potential geojaewoijeawoiej the old code name was 'Floor'.":
    floorNumb = int(input("What floor would you like to go to?: "))
    Speed = 6
    Strength = 6
    Defense = 6
    Magic = 5
    maxMana = 5 + random.randint(2, 3)
    maxHealth = 5
    Mana = maxMana
    XP = floorNumb ** 2
    XPcheck()
    Health = maxHealth
    Accuracy = 1
    EnemyLevel = floorNumb - math.ceil(floorNumb // 2)
    money = EnemyLevel / 100
    floorLevel = floorNumb
    while Health > 0:
        gameLoop()
elif AnimeSpecs:
    if Start == "goku":
        XP = 1000000
        setupPlayer()
        while Health > 0:
            gameLoop()
    elif Start == "MAHORAGA HELP ME":
        Strength += 500
        Defense += 500
        Speed += 500
        Magic = 0
        Accuracy = 100
        Health = 5
        maxHealth = 5
        print("Your stats are:")
        time.sleep(0.5)
        print(f"Health: {Health}")
        time.sleep(0.5)
        print(f"Speed: {Speed}")
        time.sleep(0.5)
        print(f"Strength: {Strength}")
        time.sleep(0.5)
        print(f"Defense: {Defense}")
        time.sleep(0.5)
        print(f"Magic: {Magic}")
        time.sleep(0.5)
        print("")
        while Health > 0:
            gameLoop()
    elif Start == "Satoru Gojo!":
        Strength = 500
        Defense = 10
        Magic = 5000
        Speed = 10000
        Accuracy = 1
        Level = 5
        Health = 5
        maxHealth = 5
        maxMana = 2500
        Mana = maxMana
        item = "Weapon"
        weapon = "Cursed Energy"
        print("Your stats are:")
        time.sleep(0.5)
        print(f"Health: {Health}")
        time.sleep(0.5)
        print(f"Speed: {Speed}")
        time.sleep(0.5)
        print(f"Strength: {Strength}")
        time.sleep(0.5)
        print(f"Defense: {Defense}")
        time.sleep(0.5)
        print(f"Magic: {Magic}")
        time.sleep(0.5)
        print("")
        while Health > 0:
            gameLoop()
    elif Start == "Fraudkuna" or Start == "the strongest in history":
        Strength = 100
        Defense = 100
        Magic = 1000
        Speed = 1000
        Accuracy = 1
        Health = 20
        maxHealth = 20
        maxMana = 2500
        Mana = maxMana
        item = "Sukuna"
        print("Your stats are:")
        time.sleep(0.5)
        print(f"Health: {Health}")
        time.sleep(0.5)
        print(f"Speed: {Speed}")
        time.sleep(0.5)
        print(f"Strength: {Strength}")
        time.sleep(0.5)
        print(f"Defense: {Defense}")
        time.sleep(0.5)
        print(f"Magic: {Magic}")
        time.sleep(0.5)
        print("")
        while Health > 0:
            gameLoop()
    elif Start == "Arlong":
        Strength = 50
        Defense = 10
        Magic = 50
        Speed = 100
        Accuracy = 1
        Level = 6
        Health = 200
        maxHealth = 200
        maxMana = 250
        Mana = maxMana
        item = "Weapon"
        weapon = "Fishman"
        print("Your stats are:")
        time.sleep(0.5)
        print(f"Health: {Health}")
        time.sleep(0.5)
        print(f"Speed: {Speed}")
        time.sleep(0.5)
        print(f"Strength: {Strength}")
        time.sleep(0.5)
        print(f"Defense: {Defense}")
        time.sleep(0.5)
        print(f"Magic: {Magic}")
        time.sleep(0.5)
        print("")
        while Health > 0:
            gameLoop()