class Commande:
    def __init__(self, num_commande):
        self.__num_commande = num_commande
        self.__plats_commandes = []
        self.__statut = "en cours"
    
    def ajouter_plat(self, plat):
        self.__plats_commandes.append(plat)
        
    def annuler_commande(self):
        self.__plats_commandes = []
        self.__statut = "annulée"
        
    def changer_statut(self, statut):
        self.__statut = statut
        
    def get_num_commande(self):
        return self.__num_commande
    
    def get_plats_commandes(self):
        return self.__plats_commandes
    
    def get_statut(self):
        return self.__statut
