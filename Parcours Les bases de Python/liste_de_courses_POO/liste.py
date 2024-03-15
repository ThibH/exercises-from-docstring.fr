"""Contains Liste class"""

import json
from pathlib import Path


class Liste:
    """A list (shopping list or anything else)"""

    def __init__(self, name: str) -> None:
        self.name = name.upper()
        self.items = []

    def __str__(self) -> str:
        items_count = len(self.items)
        return f"Liste {self.name}, contenant {items_count} élément{'s' if items_count > 1 else ''}."

    def add_to_list(self, item):
        """Adds to items an element chosen by the user."""
        self.items.append(item.lower())
        print(f"L'élément {item.upper()} a été ajouté à la liste {self.name}.")

    def remove_from_list(self, item):
        """Remove from items an element chosen by the user,
        or displays a message if the element is not in the list.
        """
        item = item.lower()
        if item in self.items:
            self.items.remove(item)
            print(f"L'élément {item.upper()} a été retiré de la liste {self.name}.")
        else:
            print(f"L'élément {item.upper()} n'est pas dans la liste {self.name}.")

    def display_list(self):
        """Displays list items, or a message saying it's empty.."""
        if self.items:
            print(f"La liste {self.name} contient:\n- "
                  + "\n- ".join(self.items))
        else:
            print(f"La liste {self.name} est vide.")

    def clear_list(self):
        """Clears list, and displays a message."""
        self.items.clear()
        print(f"La liste {self.name} a été vidée.")

    def save_list(self):
        """Save list to json format."""

        data_folder = Path.cwd() / "data"
        list_data = data_folder / f"{self.name.lower()}.json"

        data_folder.mkdir(exist_ok=True)
        with open(list_data, 'w', encoding='utf-8') as f:
            json.dump(self.items, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    l = Liste("courses")
    l.add_to_list("pommes")
    l.add_to_list("poires")
    l.save_list()
    print(l)
