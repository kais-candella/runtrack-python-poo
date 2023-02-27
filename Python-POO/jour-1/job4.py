class Personne:

    def __init__(self, nom1,prenom1,):
        self.nom1 = nom1
        self.prenom1 = prenom1
       
        
    def SePresenter(self):
        return self.nom1 + self.prenom1
       

nom1 = Personne("Jhon" ,"Doe",)
nom2 = Personne( "Jhon" , "Whick")


print("Je suis",nom1.SePresenter())
print("Je suis",nom2.SePresenter())


