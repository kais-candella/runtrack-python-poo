class student:
    
    def __init__(self,prénom,nom,student_id,):
        self._first_name = prénom
        self._last_name = nom
        self._student_id = student_id
        self._credits = 0
        self._level = self._student_Eval()
   
    #ajout etc des crédits     
    def add_crédits(self,crédits):
        if crédits > 0:
            self._credits += crédits
            
    def get_add_crédits(self):
        return self._credits  
    
    #info de l'étudiant 
    def student_info(self):
        print("Prénom :",self._first_name)
        print("Nom :",self._last_name)
        print("ID étudiant :",self._student_id)
        print("Niveau :",self._level)
        
        
    # boucle pour les niveau en fonction du score
    def _student_Eval(self):
        if self._credits >= 90:
            return "Excellent"
        elif self._credits >= 80:
            return "Trés Bien"
        elif self._credits >=70:
            return "Bien"
        elif self._credits >= 60:
            return "Passable"
        else:
            return " INSUFISANT !!"
        
        
######################################################        
        

kais = student("kais","Candella","145")

kais.add_crédits(10)
kais.add_crédits(20)
kais.add_crédits(80)

kais.student_info()
######################################################

print("Le nombre de crédit actuel de kais est de ->", kais.get_add_crédits())
print("Evaluation:", kais._student_Eval())