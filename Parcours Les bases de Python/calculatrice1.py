"""
CALCULATRICE

-> Exercise from the course "Les bases de Python" on the Docstring website (www.docstring.fr)
A very very very simple calculator that can only add integer numbers.

Date: 2024-03-02
Author: Simon Salvaing
"""

entrees_valides = False
while not entrees_valides:
      nb1 = input("Entrez un premier nombre entier: ")
      nb2 = input("Entrez un second nombre entier: ")
      entrees_valides = nb1.isdigit() and nb2.isdigit()
      if not entrees_valides:
            print("Veuillez entrer 2 nombres valides")

nb1, nb2 = int(nb1), int(nb2)
print(f"Le résultat de l'addition de {nb1} avec {nb2} est {nb1 + nb2}.")
