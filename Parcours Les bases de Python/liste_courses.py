"""
LISTE DE COURSES
-> Exercise from the course "Les bases de python" on the Docstring website (www.docstring.fr)
A program to manage a shopping list.
Date: 2024-03-03
Author: Simon Salvaing
"""

MENU = """Choisissez parmi les 5 options suivantes :
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter
👉 Votre choix : """

def display_menu() -> str:
    """Displays menu and returns user's choice."""
    choice = input(MENU)
    return choice

def add_to_list(shopping_list: list):
    """Adds to shopping list an elemnt chosen by user."""
    item = input("Entrez le nom d'un élément à ajouter à la liste de courses : ").capitalize()
    shopping_list.append(item)
    print(f"L'élément {item} a bien été ajouté à la liste.")
    
def remove_from_list(shopping_list: list):
    """Remove from shopping list an elemnt chosen by user, or displays a message
    if the element is not in the list
    ."""
    item = input("Entrez le nom d'un élément à retirer de la liste de courses : ").capitalize()
    try:
        shopping_list.remove(item)
        print(f"L'élément {item} a bien été supprimé de la liste.")
    except ValueError:
        print(f"L'élément {item} n'est pas dans la liste.")

def display_list(shopping_list: list):
    """Displays shopping list, or a message saying it's empty.."""
    if shopping_list:
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Votre liste ne contient aucun élément.")

def clear_list(shopping_list: list) -> list:
    """Clears shopping list, displays a message, and returns the empty list."""
    shopping_list.clear()
    print("La liste a été vidée de son contenu.")

def leave_program():
    """Displays a goodbye message."""
    print("À bientôt !")

def main():
    my_list = []
    choice = ""
    while choice != "5":
        choice = display_menu()
        match choice:
            case "1":
                add_to_list(my_list)
            case "2":
                remove_from_list(my_list)
            case "3":
                display_list(my_list)
            case "4":
                clear_list(my_list)
            case "5":
                leave_program()
            case _:
                print("Choix incorrect. Choisissez un nombre de 1 à 5.")
        print("-" * 50)

main()
