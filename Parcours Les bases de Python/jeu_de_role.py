"""
JEU DE RÔLE DANS LE TERMINAL
-> Exercise from the course "Les bases de Python" on the Docstring website (www.docstring.fr)
A very simple role-playing game
Date: 2024-03-04
Author: Simon Salvaing
"""

import random

STARTING_NUMBER_OF_POTIONS = 3
STARTING_LIFE_POINTS = 50

MIN_DAMAGE = 5
PLAYER_MAX_DAMAGE = 10
ENEMY_MAX_DAMAGE = 15

MIN_POTION_HEALING = 15
MAX_POTION_HEALING = 50

MESSAGE = "Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
LINE_LENGTH = len(MESSAGE) + 1

def welcome():
    """Displays a welcome message."""
    print()
    print("*" * LINE_LENGTH)
    print("JEU DE RÔLE DANS LE TERMINAL".center(LINE_LENGTH, "*"))
    print("*" * LINE_LENGTH)
    print()
    print(f"Vous et votre ennemi·e avez {STARTING_LIFE_POINTS} points de vie.")
    print(f"Vous disposez de {STARTING_NUMBER_OF_POTIONS} potions, "
          "votre ennemi·e n'en a aucune.")
    print()

def player_attack(opponent_points: int) -> int:
    """Initiates an attack by the player against the opponent.
    Returns opponent's life points."""
    player_attack = random.randint(MIN_DAMAGE, PLAYER_MAX_DAMAGE)
    opponent_points -= player_attack
    print(f"Vous infligez un dommage de {player_attack} points à votre adversaire.")
    return opponent_points

def enemy_attack(player_points: int) -> int:
    """Initiates an attack by the player against the opponent.
    Returns opponent's life points."""
    enemy_attack = random.randint(MIN_DAMAGE, PLAYER_MAX_DAMAGE)
    player_points -= enemy_attack
    print(f"Votre adversaire vous inflige un dommage de {enemy_attack} points.")
    return player_points

def drink_potion(player_points: int) -> int:
    """Add a random number of points to player"""
    healing_points = random.randint(MIN_POTION_HEALING, MAX_POTION_HEALING)
    player_points += healing_points
    print(f"Grâce à votre 🧘🏼, vous récupérez {healing_points} points de vie. 💪🏼")
    return player_points
    
def main():
    
    my_points = enemy_points = STARTING_LIFE_POINTS
    number_of_potions = STARTING_NUMBER_OF_POTIONS
    end = False

    welcome()
    
    while not end:
        
        choice = input(MESSAGE)
        print()

        if choice not in ("1", "2"):
            print("Choix invalide.")
            continue
        
        if choice == "1":
            enemy_points = player_attack(enemy_points)
            if enemy_points <= 0:
                end = True
                print("GAGNÉ ! ✌🏼")
                break

            my_points = enemy_attack(my_points)
            if my_points <= 0:
                end = True
                print("PERDU ! 😭")
                break
                   
        elif choice == "2":
            if number_of_potions:
                my_points = drink_potion(my_points)
                number_of_potions -= 1
                print(f"Il vous reste maintenant {number_of_potions} "
                    f"potion{'s' if number_of_potions > 1 else ''}.")
                my_points = enemy_attack(my_points)
            else:
                print(f"Vous avez déjà bu vos {STARTING_NUMBER_OF_POTIONS} 🧘🏼!")
                continue

        print(f"Il vous reste {my_points} points de vie, "
              f"et votre adversaire en a encore {enemy_points}.")
        print("-" * LINE_LENGTH)

main() 
