# Fonction pour compter les occurrences de lettres
def count_same_letter(list_ids):
    # Variables pour compter les occurrences de lettres
    two_same_letter = 0
    three_same_letter = 0

    # Parcours de chaque identifiant de boîte dans la liste
    for box_id in list_ids:
        # Dictionnaire pour compter les occurrences de chaque lettre
        letter_count = {}
        for letter in box_id:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

        # Vérification si l'identifiant de boîte contient des lettres qui apparaissent exactement deux ou trois fois
        if 2 in letter_count.values():
            two_same_letter += 1
        if 3 in letter_count.values():
            three_same_letter += 1

    # Renvoi du nombre d'identifiants de boîte avec des lettres répétées exactement deux fois et trois fois
    return two_same_letter, three_same_letter


# Lecture du fichier d'entrée contenant les identifiants de boîte
file = open('input.txt', 'r')
box_ids = file.readlines()

# Appel de la fonction count_same_letter pour compter les occurrences de lettres
two_same_letter, three_same_letter = count_same_letter(box_ids)

# Calcul du checksum en multipliant les nombres d'identifiants de boîte avec deux lettres répétées et trois lettres répétées
checksum = two_same_letter * three_same_letter

# Affichage du checksum
print('Le checksum est :', checksum)