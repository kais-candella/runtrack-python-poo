class Voiture:
    
    def __init__(self, marque, modele, annee, kilometrages):
        self._marque = marque
        self._modele = modele
        self._annee = annee
        self._kilometrages = kilometrages
        self._en_marche = False
        self._reservoir = 50
        
    def get_marque(self):
        return self._marque
    
    def set_marque(self, marque):
        self._marque = marque
    
    def get_modele(self):
        return self._modele
    
    def set_modele(self, modele):
        self._modele = modele
    
    def get_annee(self):
        return self._annee
    
    def set_annee(self, annee):
        self._annee = annee
    
    def get_kilometrages(self):
        return self._kilometrages
    
    def set_kilometrages(self, kilometrages):
        self._kilometrages = kilometrages
    
    def get_en_marche(self):
        return self._en_marche
    
    def set_en_marche(self, en_marche):
        self._en_marche = en_marche
    
    def get_reservoir(self):
        return self._reservoir
    
    def set_reservoir(self, reservoir):
        self._reservoir = reservoir
    
    def demarrer(self):
        if self.verifier_plein() > 5:
            self._en_marche = True
        else:
            print("Le réservoir est presque vide, veuillez faire le plein avant de démarrer.")
    
    def arreter(self):
        self._en_marche = False
    
    def verifier_plein(self):
        return self._reservoir


voiture1 = Voiture("HAMANN_X_BMW", "M3-Competition", 2022, 10000)

voiture1.set_marque("HAMANN_X_BMW")
voiture1.set_modele("M3-Competition")
voiture1.set_annee(2022)
voiture1.set_kilometrages(5000)
voiture1.set_en_marche(True)

print("Marque :", voiture1.get_marque())
print("Modèle :", voiture1.get_modele())
print("Année :", voiture1.get_annee())
print("Kilométrages :", voiture1.get_kilometrages())
print("En marche :", voiture1.get_en_marche())
print("Réservoir :", voiture1.get_reservoir())

voiture1.set_reservoir(20)
print("Réservoir après mise à jour :", voiture1.get_reservoir())

voiture1.demarrer()
print("En marche après démarrage :", voiture1.get_en_marche())

voiture1.arreter()
print("En marche après arrêt :", voiture1.get_en_marche())
