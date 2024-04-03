import random


def generer(a, b, c, d, longueur):
    mdp = ""
    while len(mdp) < longueur:
        num_choix = random.randint(0, 3) # choix de l'index
        sequence = [a,b,c,d]
        choix = sequence[num_choix] # choix de la variable lettre ou chiffre ou caracteère_spe
        car_rang = random.randint(0, len(choix)-1)
        car = choix[car_rang]
        if car not in mdp:
            mdp += car                     
    return mdp


def demander_longueur_mdp():
    message = "* Merci de saisir un caratère numérique !!! *"
    cadre = len(message)
    minimum = 11
    while True:
        longueur_str = input("Merci de définir la longueure du mot de passe"
                             f"\nSaisir une valaur entre {minimum} et {nombre_max_caractere - 2} :"
                             f"\n")
        try:
            longueur = int(longueur_str)
            if minimum <longueur <= nombre_max_caractere-2: 
                return longueur
        except:
            print()
            print(cadre * "*")
            print(message)
            print(cadre * "*")
            print()


lettre = "abcdefghijklmnopkrstuvwxyz"
lettre_maj = lettre.upper()
chiffre = "1234567890"
caractere_spe = "&é'(-è_çà)=~#}{[|`\^@]*%?,.;/:!§<>$"
global nombre_max_caractere
nombre_max_caractere = len(lettre) + len(chiffre) + len(caractere_spe) + len(lettre_maj)
nombre_car_mdp = demander_longueur_mdp()
mdp_genere = generer(lettre, lettre_maj, chiffre, caractere_spe, nombre_car_mdp)

print()
print(nombre_max_caractere)
print(mdp_genere)
f = open("clé.txt", "w")
f.write(mdp_genere)
f.close()
print()
