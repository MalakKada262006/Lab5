
classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5],
    ["Diana", 22, 13.0]
]

classe.sort(key=lambda ligne: ligne[2], reverse=True)
print("Tri par note décroissante :", classe)

somme_notes = 0
for nom, age, note in classe:
    somme_notes += note
moyenne = somme_notes / len(classe)
print("Moyenne des notes :", moyenne)

nom_recherche = "Diana"
for nom, age, note in classe:
    if nom == nom_recherche:
        print(f"{nom}: {age} ans, note {note}")
        break
else:
    print(nom_recherche, "non trouvé")

resultat = next((etudiant for etudiant in classe if etudiant[0] == "Eve"), [])
print("Résultat avec next() :", resultat)

classe_copie = classe[:]  
classe_copie[0][1] = 15   
print("Classe originale :", classe)     
print("Classe copie :", classe_copie)

import copy
classe_deep = copy.deepcopy(classe) 
classe_deep[0][1] = 20
print("Classe originale après deepcopy :", classe)
print("Classe deepcopy :", classe_deep)

classe_dict = [
    {"nom": nom, "age": age, "note": note}
    for nom, age, note in classe
]
print("Classe en dictionnaires :", classe_dict)

for etudiant in classe_dict:
    print(f"{etudiant['nom']} – {etudiant['note']}")