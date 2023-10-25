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
    


Grille([1,0,2,0,3,0,
        4,0,5,0,6,0,
        7,0,8,0,9])

#exo 2





