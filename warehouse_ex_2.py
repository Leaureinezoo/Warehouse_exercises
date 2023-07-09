def find_common_letters(box_ids):
    # Variable pour stocker les lettres communes
    result = ""

    # Parcours de chaque paire d'identifiants de boîte
    for i in range(len(box_ids)):
        for j in range(i+1, len(box_ids)):
            # Comptage des différences entre les identifiants de boîte
            diff_count = sum(c1 != c2 for c1, c2 in zip(box_ids[i], box_ids[j]))

            # Si une seule différence est trouvée
            if diff_count == 1:
                # Parcours des caractères correspondants dans les identifiants de boîte
                for c1, c2 in zip(box_ids[i], box_ids[j]):
                    # Si les caractères sont identiques, ils sont ajoutés au résultat
                    if c1 == c2:
                        result += c1

                # La fonction se termine et renvoie le résultat
                return result

    # Si aucune paire d'identifiants de boîte ne diffère d'un caractère à la même position, le résultat est une chaîne vide
    return result


# Lecture du fichier d'entrée contenant les identifiants de boîte
file = open('input.txt', 'r')
box_ids = file.readlines()

# Appel de la fonction find_common_letters pour trouver les lettres communes entre les identifiants de boîte
common_letters = find_common_letters(box_ids)

# Affichage des lettres communes
print('Les lettres communes sont :', common_letters)