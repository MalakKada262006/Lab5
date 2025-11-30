
classe = [
    ["Alice", 20, 15.5],
    ["Eve", 19, 14.0],
    ["Charlie", 21, 16.5]
]
classe.append(["Diana", 22, 13.0])
print(classe)
for index, (nom, age, note) in enumerate(classe, start=1):
    print(f"Étudiant {index} : {nom} ({age} ans) – note {note}")
age_charlie = classe[2][1]
print(age_charlie)  
classe[2][2] = 17.0 
print(classe[2])
if len(classe) > 2 and len(classe[2]) > 1:
    print("Accès à :", classe[2][1])

for etudiant in classe:
    print(etudiant[0], etudiant[2])
