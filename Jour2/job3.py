class Livre:
    
    def __init__(self,title,author,numbre_of_pages):
        self._title = title
        self._author = author
        self._numbre_of_pages = numbre_of_pages
        self._available = True


######################################################
       
          
    #verifie la disponibilité du livre
    def get_available(self):
        return self._available

    
    def vérification(self):
        return self._available == True
    
    
    #emprunter le livre
    def emprunter(self):
        if self.vérification():
            self._available = False
            print("Le livre a été emprunté.")
        else:
            print("Désolé, le livre n'est pas disponible pour le moment.")
    
            
######################################################   

    #pour rendre le livre 
    def rendre(self):
        if not self.vérification():
            self._available = True
            print("Le livre a été rendu")
        else:
            print("Le livre n'a pas été emprunté ")
######################################################

livre1 = Livre("Les Misérables", "Victor Hugo", 1630)
livre2 = Livre("Au Bonheur des Dames","Emile Zole",544)



######################################################

print("Le livre est dispo  ?->", livre1.get_available())
print("Le livre est dispo  ? ->", livre2.get_available())

######################################################

livre1.emprunter()

print("Le livre est dispo  ? ->",livre1.get_available())

######################################################

livre1.rendre()
print("Le livre est dispo  ? ->",livre1.get_available())
