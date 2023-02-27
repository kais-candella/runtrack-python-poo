#afficher les coordonées X,Y
class Point:

    def __init__(self,coX,coY):
        self.coordonéeX = coX
        self.coordonéeY = coY
        

    def AfficherLesPoints(self):
       return self.coordonéeX, self.coordonéeY
    
    def afficherX(self):
        return self.coordonéeX
    
    def afficherY(self):
        return self.coordonéeY
    
    def changerX(self):
        coX = Point(20,100)


coX = Point(10,100)

print(coX.AfficherLesPoints())

coY = Point(10,100)

#afficher la coordonées X
print("-"*5)

print("X",coX.coordonéeX)

#afficher la coordonées Y
print("-"*5)

print("Y",coY.afficherY())