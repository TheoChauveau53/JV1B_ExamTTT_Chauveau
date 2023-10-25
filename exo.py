#exo 1
def Grille(tableau):
    for i in range(5):
        if i%2==0:
            for n in range(5):
                if n%2==0:
                    if(i==0):
                        print(tableau[n],end="")
                    if(i==2):
                        print(tableau[n+6],end="")
                    if(i==4):
                        print(tableau[n+12],end="")
                else:
                    print("|",end="")
            print()
        else:
            for n in range(5):
                print("_",end="")
            print()
    

grilleDeJeu = [1,0,2,0,3,0, #6 éléments par ligne
               4,0,5,0,6,0,
               7,0,8,0,9,0]

#exo 2
def Jouer(tableau, joueur, case):
    if case==1:
        tableau[0] = joueur
    if case ==2:
        tableau[2] = joueur
    if case ==3:
        tableau[4] = joueur
    if case ==4:
        tableau[6] = joueur
    if case ==5:
        tableau[8] = joueur
    if case ==6:
        tableau[10] = joueur
    if case ==7:
        tableau[12] = joueur
    if case ==8:
        tableau[14] = joueur
    if case ==9:
        tableau[16] = joueur


#exo 3 
def Verifierligne(tableau):
    if tableau[0]== tableau[2]==tableau[4]:
        return True
    if tableau[6]== tableau[8]==tableau[10]:
        return True
    if tableau[12]== tableau[14]==tableau[16]:
        return True
def Verifiercolonne(tableau):
    if tableau[0]== tableau[6]==tableau[12]:
        return True
    if tableau[2]== tableau[8]==tableau[14]:
        return True
    if tableau[4]== tableau[10]==tableau[16]:
        return True
def Verifierdiago(tableau):
    if tableau[0]== tableau[8]==tableau[16]:
        return True
    if tableau[4]== tableau[8]==tableau[12]:
        return True

def Verifier(tableau):
    if Verifiercolonne(tableau) == True or Verifierdiago(tableau) == True or Verifierligne(tableau) == True:
        return True
    
#exo 4

def VerifGrilleComplete(tableau):
    if tableau[0] != 1 and tableau[2] != 2 and tableau[4] != 3 and tableau[6] != 4 and tableau[8] != 5 and tableau[10] != 6 and tableau[12] != 7 and tableau[14] != 8 and tableau[16] != 9:
        return True

#exo 5
def VerifCase(tableau,case):
    if tableau[]


end= False
joueur = "X"
Grille(grilleDeJeu)
while(end==False):
    choix = input("ou jouer?")
    if choix =="1" or choix =="2" or choix =="3" or choix =="4" or choix =="5" or choix =="6" or choix =="7" or choix =="8" or choix =="9":
        choix = int(choix)
        Jouer(grilleDeJeu,joueur,choix)
        Grille(grilleDeJeu)
        if Verifier(grilleDeJeu) == True:
            print("Le joueur", joueur, " a gagné.")
            end = True
        elif VerifGrilleComplete(grilleDeJeu) == True:
            print("La grille est complète, il y a égalite")
            end= True 
        if joueur == "X":
            joueur= "O"
        elif joueur=="O":
            joueur = "X"
    else: 
        print("mauvais choix, choisissez une possiblité")



#exo 6
'''Pour faire un jeu de puissance 4, il suffit de laisser au joueur le choix de la colonne et non celui de la case, de verifier 
si le coup est jouable(si la colonne est pleine). Le jeton joué devra donc etre sur la case la plus basse disponible.
Il faudra aussi agrandir la grille de jeu et changer la verification de condition
de victoire afin qu'elle repère si 4 jetons du meme joueur sont alignés et non 3 comme ici.'''