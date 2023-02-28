#la Class Rectangle 
class Rectangle:
    
    def __init__(self,longueur,largeur):
        self._longueur = longueur
        self._largeur = largeur
    

#ceci est un accesseur  
    def get_longueur(self):
        return self._longueur
    
#ceci est un mutateur     
    def set_longueur(self,longueur):
        self._longueur = longueur
    
 #ceci est un accesseur     
    def get_largeur(self):
        return self._largeur
    
#ceci est un mutateur     
    def set_largeur(self,largeur):
        self._largeur = largeur

#cree un rectangle avec longueur 10 et largeur 5 
rectangle = Rectangle(10,5)


#affiche les premiere valeur ecrite dans {rectangle = Rectangle(10,5)}
print("largeur :", rectangle.get_largeur ())
print("longueur : ", rectangle.get_longueur())

#recupere les nouvelle valeur et les changes 

rectangle.set_largeur(10)
rectangle.set_longueur(20)

#afficher les nouvelles valeur 

print("largeur : " , rectangle.get_largeur())
print("longueur : ", rectangle.get_longueur())