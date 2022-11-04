largeur = 180
hauteur = 120
couleurs = ["#fff", "#000", "#f00", "#ff0", "#0f0", "#00f", "#f0f"]

# Retourne un tableau des caractéristiques des boutons
# [struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18),
# couleur='#fff', effacer=True), 
# struct(coin1=struct(x=60, y=6), coin2=struct(x=72, y=18),
# couleur='#f00', effacer=False), 
# struct(coin1=struct(x=78, y=6), coin2=struct(x=90, y=18),
# couleur='#ff0', effacer=False), 
# struct(coin1=struct(x=96, y=6), coin2=struct(x=108, y=18),
# couleur='#0f0', effacer=False), 
# struct(coin1=struct(x=114, y=6), coin2=struct(x=126, y=18),
# couleur='#00f', effacer=False), 
# struct(coin1=struct(x=132, y=6), coin2=struct(x=144, y=18),
# couleur='#f0f', effacer=False)]
def creerBoutons(couleurs, taille, espace, couleurEffacer):
    # Le tableau contient automatiquement les caractéristiques
    # du bouton effacer
    boutons = [struct(coin1=struct(x=6, y=6), coin2=struct(x=18, y=18),
              couleur="#fff", effacer=True)]
    # Ajoute les caractéristiques des autres boutons
    for i in range(len(couleurs)):
            boutons.append(struct(coin1=struct(x=(i+2)*taille 
            + i * espace, y=6), coin2=struct(x=(i+3)*taille + 
            i * espace, y=18), couleur=couleurs[i], effacer=False))
    return boutons
 
# Retourne les caractéristiques d'un bouton du tableau selon
# la position choisie
# struct(coin1=struct(x=24, y=6), coin2=struct(x=36, y=18), couleur='#fff',
# effacer=False)
def trouverBouton(boutons, position):
    for i in range(len(boutons)):
        x1 = boutons[i].coin1.x
        y1 = boutons[i].coin1.y
        x2 = boutons[i].coin2.x
        y2 = boutons[i].coin2.y
        #Recherche si la position choisie est dans un des boutons du tableau
        for j in range(x1, x2):
            for k in range(y1, y2):
                if j == position[0] and k == position[1]:
                    return boutons[i]
    return None 
    
# Procédure qui permet de dessiner un bouton    
def dessinerBouton(taille, espace, position):
    # Trouve le bouton à dessiner en fonction de la position choisie
    bouton = trouverBouton(creerBoutons(["#fff", "#000", "#f00", "#ff0",
             "#0f0", "#00f", "#f0f"], taille, espace, "#fff"), position)
    # Dessine le rectangle du bouton avec la bonne couleur
    fillRectangle(bouton.coin1.x, bouton.coin1.y, taille, taille,
    bouton.couleur)
    # Dessine le X du bouton effacer
    if bouton.effacer == True:
        for i in range(taille):
            for j in range(taille):
                if i == j:
                    fillRectangle(bouton.coin1.x+i, bouton.coin1.y+j, 
                    1, 1, "#f00")
                    fillRectangle(bouton.coin1.x+i, bouton.coin2.y-j, 
                    1, 1, "#f00")
    # Dessine le contour de 1px du bouton
    fillRectangle(bouton.coin1.x, bouton.coin1.y, taille, 1, "#000")
    fillRectangle(bouton.coin2.x, bouton.coin1.y, 1, taille, "#000")
    fillRectangle(bouton.coin1.x, bouton.coin2.y, taille + 1, 1, "#000")
    fillRectangle(bouton.coin1.x, bouton.coin1.y, 1, taille, "#000")

# Appels pour dessiner les huit boutons


# Dessine un rectangle au clic de l'utilisateur jusqu'à ce qu'il relache
# le bouton de la souris (À compléter)
def dessinerRectangleFlottant(imageOriginale, debut, couleur):
    boucle1 = True
    # Boucle qui balaie la grille
    while boucle1 == True:
            getMouse()
            # Lorsque l'utilisateur clique
            if getMouse().button == 1:
                positionInitiale = getMouse()
                boucle2 = True
                # Continue de balayer
                while boucle2 == True:
                   # imageOriginale1 = imageOriginale
                    getMouse()
                    # Dessine un nouveau rectangle à chaque 0.01 seconde
                    positionIntermediaire = getMouse()
                    fillRectangle(positionInitiale.x, positionInitiale.y,
                      positionIntermediaire.x - positionInitiale.x,
                      positionIntermediaire.y - positionInitiale.y, couleur)
                    #positionRetrait = getMouse()
                   # if positionRetrait.x < positionIntermediaire.x:
                    #    for i in range(180):
                     #       for j in range(120):
                      #          setPixel(i,j,imageOriginale1[i][j])
                    
                    sleep(0.01) 
                     
                     # Lorsque l'utilisateur relache le bouton, on obtient le
                     # rectangle final
                    if getMouse().button == 0:
                        boucle2 = False
            trouverBouton(creerBoutons(couleurs, 12, 6, "#fff"), [getMouse().x, getMouse().y])
            if trouverBouton(creerBoutons(couleurs, 12, 6, "#fff"), [getMouse().x, getMouse().y]) == None:
                continue
            elif trouverBouton(creerBoutons(couleurs, 12, 6, "#fff"), [getMouse().x, getMouse().y]).couleur != couleur:
                break 
            sleep(0.01)
               
def traiterProchainClic(boutons): 
    boucle3 = True
    while boucle3 == True:
        getMouse()
        if getMouse().button == 1:
            bouton = trouverBouton(boutons, [getMouse().x, getMouse().y])
            if bouton == None:
                continue
            elif bouton.couleur == "#fff":
                dessinerRectangleFlottant(1, 1, bouton.couleur)
            elif bouton.couleur == "#000":
                dessinerRectangleFlottant(1, 1, bouton.couleur)
            elif bouton.couleur == "#f00":
                dessinerRectangleFlottant(1, 1, bouton.couleur)
            elif bouton.couleur == "#ff0":
                dessinerRectangleFlottant(1, 1, bouton.couleur)
            elif bouton.couleur == "#0f0":
                dessinerRectangleFlottant(1, 1, bouton.couleur)
            elif bouton.couleur == "#00f":
                dessinerRectangleFlottant(1, 1, bouton.couleur)
            elif bouton.couleur == "#f0f":
                dessinerRectangleFlottant(1, 1, bouton.couleur)
    
    
def dessiner():
    setScreenMode(largeur, hauteur)
    fillRectangle(0, 0, largeur, hauteur, "#fff")
    fillRectangle(0, 0, largeur, 24, "#888")
    dessinerBouton(12, 6, [7, 10])
    dessinerBouton(12, 6, [25, 10])
    dessinerBouton(12, 6, [43, 10])
    dessinerBouton(12, 6, [61, 10])
    dessinerBouton(12, 6, [79, 10])
    dessinerBouton(12, 6, [97, 10])
    dessinerBouton(12, 6, [115, 10])
    dessinerBouton(12, 6, [133, 10])      
   # procImageOriginale()
    traiterProchainClic(creerBoutons(["#fff", "#000", "#f00", "#ff0",
             "#0f0", "#00f", "#f0f"], 12, 6, "#fff"))


    
    
def procImageOriginale():
    imageOriginale = []
    for i in range(180):
        imageOriginale.append([])
        for j in range(120):
            imageOriginale[i].append(getPixel(i,j))
    return imageOriginale
        
    
dessiner()