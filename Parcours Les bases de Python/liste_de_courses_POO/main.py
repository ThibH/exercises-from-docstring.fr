"""
LISTE DE COURSES VERSION ORIENTÉ OBJET
-> Exercise from the course "Les bases de python" on the Docstring website (www.docstring.fr)
A program to manage a to-do list using OOP.
Date: 2024-03-11
Author: Simon Salvaing
"""

from functions import display_menu, OPTIONS


def main():
    choice = -1
    while choice != 8:

        try:
            choice = int(display_menu())
        except ValueError:
            print("Choix invalide.")
            continue

        OPTIONS[choice]["function"]()

        print()
        print("-" * 50)
        print()


if __name__ == '__main__':
    main()
