"""Constants and functions used in main.py"""

import json
from collections import OrderedDict
from pathlib import Path

import liste

# Menu options:
OPTIONS = OrderedDict([
    ("INDEX", "Consulter l'index des listes existantes"),
    ("CONTENT", "Consulter le contenu d'une liste"),
    ("CREATE", "Créer une nouvelle liste"),
    ("ADD", "Ajouter un élément à une liste"),
    ("REMOVE", "Retirer un élément à une liste"),
    ("CLEAR", "Effacer tout le contenu d'une liste"),
    ("DELETE", "Supprimer une liste"),
    ("QUIT", "Quitter le programme"),
    ])

OPTIONS_STR = f"\n".join([f"{i}: {OPTIONS[key]}"  for i, key in enumerate(OPTIONS, 1)])

MENU = f"""Choisissez parmi les {len(OPTIONS)} options suivantes :
{OPTIONS_STR}
👉 Votre choix : """

DATA_FOLDER = Path.cwd() / "data"

def display_menu() -> str:
    """Displays menu and returns user's choice."""
    choice = input(MENU)
    print()
    return choice

def lists_index_consulting():
    """Displays all the available lists names.
    A list is available if a .json file with the same lowercased name exists
    in the data folder.
    """
    files = DATA_FOLDER.glob("*.json")
    lists_index = [file.stem for file in files]

    if lists_index:
        print("Voici l'ensemble des listes disponibles:")
        for item in lists_index:
            print(item.upper())
    else:
        print("Aucune liste n'est créée pour le moment.")

def list_content_consulting():
    """Ask which list to consult, and displays its content
    (or an error message if list name given by the user doesn't exist)
    """
    name = input("Quelle liste voulez-vous consulter ? ").lower()
    files_names = [file.stem for file in DATA_FOLDER.glob("*.json")]
    if name in files_names:
        list_file = DATA_FOLDER / f"{name}.json"
        with open(list_file, 'r', encoding='utf-8') as lf:
            l = liste.Liste(name)
            l.items = json.load(lf)
            l.display_list()
    else:
        print(f"Aucune liste ne porte le nom {name.upper()}.")

def creates_list():
    name = input("Quel nom voulez-vous donner à la liste ? ")
    files_names = [file.stem for file in DATA_FOLDER.glob("*.json")]
    if name not in files_names:
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
    files_names = [file.stem for file in DATA_FOLDER.glob("*.json")]
    if name in  files_names:
        list_file = DATA_FOLDER / f"{name}.json"
        with open(list_file, 'r', encoding='utf-8') as lf:
            l = liste.Liste(name)
            l.items = json.load(lf)
            item = input("Que vous-vous ajouter à la liste ? ")
            l.add_to_list(item)
            l.save_list()
    else:
        print(f"La liste {name.upper()} n'existe pas.")

def remove_from_list():
    """Remove an item from a list, then saves the list.
    If list doesn't exist, displays an error message.
    """
    name = input("À quelle liste voulez-vous retirer un élément ? ").lower()
    files_names = [file.stem for file in DATA_FOLDER.glob("*.json")]
    if name in  files_names:
        list_file = DATA_FOLDER / f"{name}.json"
        with open(list_file, 'r', encoding='utf-8') as lf:
            l = liste.Liste(name)
            l.items = json.load(lf)
            item = input("Que vous-vous retirer de la liste ? ")
            l.remove_from_list(item)
            l.save_list()
    else:
        print(f"La liste {name.upper()} n'existe pas.")

def clear_list():
    """Clears a list
    """
    name = input("Quelle liste voulez-vous vider ? ").lower()
    files_names = [file.stem for file in DATA_FOLDER.glob("*.json")]
    if name in  files_names:
        list_file = DATA_FOLDER / f"{name}.json"
        with open(list_file, 'w', encoding='utf-8') as lf:
            l = liste.Liste(name)
            l.clear_list()
            l.save_list()
    else:
        print(f"La liste {name.upper()} n'existe pas.")

def delete_list():
    """Delete a list file
    """
    name = input("Quelle liste voulez-vous supprimer définitivement ? ").lower()
    files_names = [file.stem for file in DATA_FOLDER.glob("*.json")]
    if name in  files_names:
        list_file = DATA_FOLDER / f"{name}.json"
        list_file.unlink()
        print(f"La liste {name.upper()} a été supprimée de vos fichiers.")
    else:
        print(f"La liste {name.upper()} n'existe pas.")

def quit_programm():
    """Displays a goodbye message."""
    print("À bientôt !")


if __name__ == "__main__":
    print(MENU)
