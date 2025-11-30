classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5],
    ["Diana", 22, 13.0]
]
nouveaux = [
    ["Aslan", 23, 12.5],
    ["Ayhan", 20, 17.0]
]
classe.extend(nouveaux)  
print("Classe après extend :", classe)
notes_bonnes = [note for _, _, note in classe if note >= 15]
print("Notes >= 15 :", notes_bonnes)
import pprint
pprint.pprint(classe)
