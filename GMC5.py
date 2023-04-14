import numpy as np
etudiant= int(input("saisir le nombre d'etudiants"))
matiere= int(input("saisir le nombre de matiéres"))
tableau= np.array([[],[]])
print(tableau)

for i in range(etudiant):
    my_list = []
    for j in range(matiere):
        a= int(input(f"saisir la note de la matiére {j+1} de l'etudiant {i+1}"))
        my_list.append(a)
    tableau=np.append(tableau, my_list)
print(tableau)
tableau=tableau.reshape(etudiant, matiere)
print(tableau)
total=(np.sum(tableau,axis=1))
pourcentage = (total / (matiere * 100)) * 100
note=[]
for i in pourcentage:
    if i >= 90:
        note.append("a+")
    elif i >= 80:
        note.append("a")
    elif i >= 70 :
        note.append("b+")
    elif i >= 60:
        note.append("b")
    elif i >= 50:
        note.append("c")
    else:
        note.append("f")

print("{:<10} {:<12} {:<12} {:<10}".format("etudiant", "total", "pourcentage", "note"))
for i in range(etudiant):
    print("{:<10} {:<12} {:<12.2f} {:<10}".format(i+1, total[i], pourcentage[i], note[i]))