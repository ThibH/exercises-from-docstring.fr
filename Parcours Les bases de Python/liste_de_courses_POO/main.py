"""
LISTE DE COURSES VERSION ORIENTÉ OBJET
-> Exercise from the course "Les bases de python" on the Docstring website (www.docstring.fr)
A program to manage a to-do list using OOP.
Date: 2024-03-11
Author: Simon Salvaing
"""

import functions as f

options = list(f.OPTIONS.keys())

def main():
    choice = ""
    while choice != str(options.index("QUIT") + 1):
        choice = f.display_menu()
        if choice == str(options.index("INDEX") + 1):
            f.lists_index_consulting()
        elif choice == str(options.index("CONTENT") + 1):
            f.list_content_consulting()
        elif choice == str(options.index("CREATE") + 1):
            f.creates_list()
        elif choice == str(options.index("ADD") + 1):
            f.add_to_list()
        elif choice == str(options.index("REMOVE") + 1):
            f.remove_from_list()
        elif choice == str(options.index("CLEAR") + 1):
            f.clear_list()
        elif choice == str(options.index("DELETE") + 1):
            f.delete_list()
        elif choice == str(options.index("QUIT") + 1):
            f.quit_programm()
        else:
            print("Choix invalide.")
        print()
        print("-" * 50)
        print()

main()
