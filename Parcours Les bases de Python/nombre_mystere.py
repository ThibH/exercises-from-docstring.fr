"""
MYSTERY NUMBER GAME

-> Exercise from the course "Les bases de Python" on the Docstring website (www.docstring.fr)
A game where the player has to guess a random number beetween 1 and 100 number within 5 attempts.

Date: 2024-03-04
Author: Simon Salvaing
"""

import random

MYSTERY_NUMBER = random.randint(1, 100)
MAX_NUMBER_OF_ATTEMPTS = 5

def main():

    print("🕹️  Le jeu du nombre mystère 🕹️")

    nb_of_attempts = 0
    win = False

    while not win and nb_of_attempts < MAX_NUMBER_OF_ATTEMPTS:
        remaining_attempts = MAX_NUMBER_OF_ATTEMPTS - nb_of_attempts
        orth_essai = "essais" if remaining_attempts > 1 else "essai"
        print(f"Il te reste {remaining_attempts} {orth_essai}.")
        choice = input("Devine le nombre entre 1 et 100 : ")

        valid_choice = choice.isdigit() and int(choice) in range(1, 101)
        if not valid_choice:
            print("Veuillez entrer un nombre valide.")
            continue

        choice = int(choice)
        nb_of_attempts += 1
        if choice < MYSTERY_NUMBER:
            print(f"Le nombre mystère est plus grand que {choice}.")
        elif choice > MYSTERY_NUMBER:
            print(f"Le nombre mystère est plus petit que {choice}.")
        else:
            win = True
            orth_essai = "essais" if nb_of_attempts > 1 else "essai"
            print()
            print(f"🍾🍾🍾 GAGNÉ ! Tu as trouvé le nombre mystère en "
                  f"{nb_of_attempts} {orth_essai}. 🍾🍾🍾")

    if not win:
        print()
        print(f"😹😹😹 PERDU ! Le nombre mystère était: {MYSTERY_NUMBER}.")

    print("Fin du jeu.")

main()

