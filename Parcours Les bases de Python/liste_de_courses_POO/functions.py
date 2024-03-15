"""Constants and functions used in main.py

CORRECTION : La chose la plus importante : éviter la répétition de code.
Pour ça j'ai créé une fonction `get_existing_lists` qui retourne les listes disponibles.
Tu répétais cette ligne de code au moins 5 fois, même si ce n'est qu'une ligne de code,
il est préférable de l'englober dans une fonction pour n'avoir à changer le code qu'à un seul endroit
(si par exemple par la suite tu changeais le format et n'utilisais plus du .json par exemple).
Pareil pour la lecture et écriture de la liste : j'ai créé 2 fonctions dédiées à cela.
Ça permet de rassembler cette logique à un seul et même endroit et éviter la répétition.
"""

import json
from pathlib import Path

import liste

# Attention avec Path.cwd, ça retourne le chemin courant à partir duquel tu exécutes le script.
# Ce chemin peut ne pas correspondre à celui du script lui-même (je peux exécuter ton script depuis
# n'importe où dans mon système de fichiers). À la place, utilise `__file__` qui retourne le chemin
# absolu du fichier actuel.
DATA_FOLDER = Path(__file__).parent / "data"
print(DATA_FOLDER)


def load_list(name: str) -> liste.Liste:
    """Charge une liste à partir d'un fichier JSON."""
    list_file = DATA_FOLDER / f"{name}.json"
    with open(list_file, 'r', encoding='utf-8') as lf:
        items = json.load(lf)
    l = liste.Liste(name)
    l.items = items
    return l


def save_list(list_obj: liste.Liste):
    """Sauvegarde une liste dans un fichier JSON."""
    list_file = DATA_FOLDER / f"{list_obj.name}.json"
    with open(list_file, 'w', encoding='utf-8') as lf:
        json.dump(list_obj.items, lf)


def display_menu() -> str:
    """Displays menu and returns user's choice."""
    return input(MENU)


def get_existing_lists() -> list:
    """Returns a list of existing list names."""
    return [file.stem for file in DATA_FOLDER.glob("*.json")]


def display_available_lists():
    """Displays all the available lists names.
    A list is available if a .json file with the same lowercased name exists
    in the data folder.
    """
    files = DATA_FOLDER.glob("*.json")
    # Nouveauté de Python 3.9 : walrus operator
    if lists_index := [file.stem for file in files]:
        print("Voici l'ensemble des listes disponibles:")
        for item in lists_index:
            print(item.upper())
    else:
        print("Aucune liste n'est créée pour le moment.")


def display_list_content():
    """Ask which list to consult, and displays its content
    (or an error message if list name given by the user doesn't exist)
    """
    name = input("Quelle liste voulez-vous consulter ? ").lower()
    if name in get_existing_lists():
        l = load_list(name)
        l.display_list()
    else:
        print(f"Aucune liste ne porte le nom {name.upper()}.")


def create_new_list():
    name = input("Quel nom voulez-vous donner à la liste ? ")
    if name not in get_existing_lists():
        l = liste.Liste(name)
        l.save_list()
        print(f"La liste {name.upper()} a été créée.")
    else:
        print(f"La liste {name.upper()} eiste déjà !")


def add_to_list():
    """Add an item to a list, then saves the list.
    If list doesn't exist, displays an error message.
    """

    name = input("À quelle liste voulez-vous ajouter un élément ? ").lower()
    files_names = get_existing_lists()
    if name in files_names:
        l = load_list(name)
        item = input("Que voulez-vous ajouter à la liste ? ")
        l.add_to_list(item)
        save_list(l)
    else:
        print(f"La liste {name.upper()} n'existe pas.")


def remove_from_list():
    """Remove an item from a list, then saves the list.
    If list doesn't exist, displays an error message.
    """

    name = input("À quelle liste voulez-vous retirer un élément ? ").lower()
    files_names = get_existing_lists()
    if name in files_names:
        l = load_list(name)
        item = input("Que voulez-vous retirer de la liste ? ")
        l.remove_from_list(item)
        save_list(l)
    else:
        print(f"La liste {name.upper()} n'existe pas.")


def clear_list():
    """Clears a list
    """
    name = input("Quelle liste voulez-vous vider ? ").lower()
    if name in get_existing_lists():
        l = load_list(name)
        l.clear_list()  # Supposons que cette méthode vide la liste en interne.
        save_list(l)
        print(f"La liste {name.upper()} a été vidée.")
    else:
        print(f"La liste {name.upper()} n'existe pas.")


def delete_list():
    """Delete a list file
    """
    name = input("Quelle liste voulez-vous supprimer définitivement ? ").lower()
    if name in get_existing_lists():
        list_file = DATA_FOLDER / f"{name}.json"
        list_file.unlink()
        print(f"La liste {name.upper()} a été supprimée de vos fichiers.")
    else:
        print(f"La liste {name.upper()} n'existe pas.")


def quit_program():
    """Displays a goodbye message."""
    print("À bientôt !")


# Menu options:
OPTIONS = {
    1: {"display": "Consulter l'index des listes existantes", "function": display_available_lists},
    2: {"display": "Consulter le contenu d'une liste", "function": display_list_content},
    3: {"display": "Créer une nouvelle liste", "function": create_new_list},
    4: {"display": "Ajouter un élément à une liste", "function": add_to_list},
    5: {"display": "Retirer un élément à une liste", "function": remove_from_list},
    6: {"display": "Effacer tout le contenu d'une liste", "function": clear_list},
    7: {"display": "Supprimer une liste", "function": delete_list},
    8: {"display": "Quitter le programme", "function": quit_program},
}  # Depuis Python 3.7 les dictionnaires sont ordonnés par défaut, plus besoin de OrderedDict.

OPTIONS_STR = "\n".join(f"{key} - {value['display']}" for key, value in OPTIONS.items())

MENU = f"""Choisissez parmi les {len(OPTIONS)} options suivantes :
{OPTIONS_STR}
👉 Votre choix : """

if __name__ == "__main__":
    print(MENU)
