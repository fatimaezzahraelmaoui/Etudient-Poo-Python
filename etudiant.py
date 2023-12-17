class Etudiant:
    def __init__(self,nom,note1,note2):
        self.__nom = nom
        self.__note1 = note1
        self.__note2 = note2
    def getnom(self):
        return self.__nom
    def setnom(self,nom):
        self.__nom = nom
    def getnote1(self):
        return self.__note1
    def setnote1(self,note1):
        self.__note1 = note1
    def getnote2(self):
        return self.__note2
    def setnote2(self,note2):
        self.__note2 = note2
        
    def calc_moy(self):
        self.calc_moy = (self.__note1 + self.__note2)/2
        return self.calc_moy
    def afficherInfo(self):
        print("le nom est :",self.__nom )
        print("la note1 est :", self.__note1)
        print("la note2 est :",self.__note2)
        print("le moyenne des notes est :",self.calc_moy)
    
"""Etu1 = Etudiant("hafssa",15,17)
print(Etu1.calc_moy())
Etu1.afficherInfo()"""
nom = input("Entrer le nom: ")
note1= int(input("Entrer la note 1: "))
note2= int(input("Entrer la note 2: "))
E = Etudiant (nom, note1, note2)
print(E.calc_moy())
E.afficherInfo()


