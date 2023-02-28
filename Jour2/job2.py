class Livre:
    
    def __init__(self,title,author,numbre_of_pages):
        self._title = title
        self._author = author
        self._numbre_of_pages = numbre_of_pages

####################################################
   
    #pour le titre ->accesseur
    def get_title(self):
        return self._title
    #pour le titre ->mutateur
    def set_title(self,title):
        self._title = title
        
#####################################################

   #pour l'auteur ->accesseur
    def get_author(self):
        return self._author
    
    #pour l'auteur -> mutateur
    def set_author(self,author):
        self._author = author

#####################################################        
   
    #pour le titre ->accesseur
    def get_numbre_of_pages(self):
        return self._numbre_of_pages
    
    #pour le titre ->mutateur
    def set_numbre_of_pages(self, numbre_of_pages):
        self._numbre_of_pages = numbre_of_pages
        
######################################################
       
pages = Livre("Mon Livre", "Moi", 1630)
author = Livre("Les misérable", "Victor Hugo", 1630)
title = Livre("Les misérable", "Victor Hugo",1630)

######################################################



#pour l'auteur du livre 
print("the author is " ,author.get_author())

#pour le titre du livre
print("the title is : ", title.get_title())

#pour le nombre de page 
print("the numbre of pages in this book is :", pages.get_numbre_of_pages())



######################################################


title.set_title("Au Bonheur des Dames")
pages.set_numbre_of_pages(544)
author.set_author("Emile Zole")

######################################################

print("the author is ",author.get_author())

#pour le titre du livre
print("the title is ",title.get_title())

#pour le nombre de page 
print("this book have", pages.get_numbre_of_pages(),"pages")