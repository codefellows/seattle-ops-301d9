# Ops Challenge - Python Conditionals

## Demo Code

The demo code below introduces concepts necessary to complete the challenge.

```python
#!/usr/bin/env python3
# Script:                       Op Challenge 10
# Author:                       Hexx King
# Date of latest revision:      05/18/2023
# Purpose:                      Python Conditionals

# Video Game Challenge

# Prompt the user for character attributes
player_class = input("Choose your character class (mage/warrior/archer): ")
enemy_health = int(input("Enter the enemy's health (integer): "))
player_health = int(input("Enter your health (integer): "))
enemy_strength = input("Enter the enemy's strength (boss/regular): ").lower()
boss_shield_active = input("Is the boss's shield active? (yes/no): ").lower() == "yes"

# Main

# if statement
if player_class == "mage":
    print("You have selected the mage class. Prepare your spells!")

# if-else statement
if enemy_strength == "boss":
    print("You are facing a powerful boss enemy!")
else:
    print("You are encountering a regular enemy.")

# if-elif-else statement
if player_health >= 80:
    print("You are in great shape for this battle!")
elif player_health >= 50:
    print("Your health is decent, but be cautious!")
else:
    print("Your health is low. Consider healing before the fight.")

# Nested if statement
if boss_shield_active:
    print("The boss has an energy shield.")
    if player_class == "mage":
        print("As a mage, you can try to dispel the shield with your magic.")
    else:
        print("You may need a special weapon to break the shield.")
else:
    print("The boss's shield is down. Attack now!")

# Complex logical condition
if (enemy_strength == "boss" and boss_shield_active) or (enemy_health > 80 and player_health < 30):
    print("This battle is extremely challenging! Be very careful.")
elif enemy_strength != "boss" and player_health > 70 and player_class != "warrior":
    print("You have the advantage. Crush your opponent!")
else:
    print("Prepare for a standard battle.")

# End
```