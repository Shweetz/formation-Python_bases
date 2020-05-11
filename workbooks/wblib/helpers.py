"""
Ceci est un module destiné à recevoir le code des fonctions mutualisées au sein
des notebooks. Vous pouvez y ajouter les fonction set les ressources que vous
pensez utiles.

Notez que dans un projet *normal* un module de ce type ne devrait être dédié
qu'à une seule unité fonctionnelle. Dans le cadre de la formation, nous allons
nous permettre de transgresser ce principe. Mais vous pouvez évidemment créer
d'autres modules (fichiers texte avec l'extension .py).

Notez également que ce commentaire est une documentation du module. Il s'agit
d'une docstring du module.
"""


def duration_for(how_many: int, unit_duration=7):
    """
    Calcul d'une durée totale en fonction d'une durée unitaire

    :param how_many: Le nombre d'unités, doit être positif ou nul
    :param unit_duration:
    :return:
    :raise ValueError: Si les valeur sont négatives
    """
    how_many = int(how_many)
    unit_duration = int(unit_duration)

    if how_many < 0:
        raise ValueError("Quantities should be positive")
    if unit_duration < 0:
        raise ValueError("Duration should be positive")

    if how_many >= 0 and unit_duration >= 0:
        return how_many * unit_duration

print(duration_for("5"))