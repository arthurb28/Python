#openclassrooms

def produit_entiers(liste_entiers):
    # écrivez le code ici
    resultat = 1
    for chiffres in liste_entiers :
        resultat *= chiffres
    return resultat 

x = [1, 2, 3, 4]
print(produit_entiers(x))

