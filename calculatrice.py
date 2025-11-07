#Demandez à l'utilisateur de fournir deux nombres avec la fonction input. 
#Stockez ces valeurs dans  nombre1et  nombre2.
nombre1 = input("veuillez fournir un nombre")
nombre2 = input("veuillez fournir un nombre")

if not nombre1.isnumeric() or not nombre2.isnumeric():
	print("les nombres ne sont pas numériques")
	raise SystemExit("Fin du programme")

nombre1 = int(nombre1)
nombre2 = int(nombre2)

operation = input("entrez l'opération souhaitez (+, -, * ou /)")
if operation not in ["+", "-", "*", "/"] :
	print("erreur, le calcul ne contient pas les signes demandés")
	raise SystemExit("Fin du programme")

if operation  == "+":
	resultat = nombre1+nombre2

elif operation == "-": 
	resultat = nombre1-nombre2

elif operation == "*":
	resultat = nombre1*nombre2

elif operation == "/" :
	if nombre2 == 0:
		print("impossible de visier pas zéro") 
		raise SystemExit("Fin du programme")

	resultat = round(nombre1 / nombre2, 2)

# Affiche le résultat
print(f"Le résultat de l'opération est: {round(resultat, 2)}")
