class Date:
    
    def __init__(self, jour=1, mois=1, annee=1970):
        self.jour=jour
        self.mois=mois
        self.annee=annee
        
    def __str__(self):
        return str(self.jour) + '/' + str(self.mois) + '/' + str(self.annee)
    
    def __lt__(self,d):
        if self.annee < d.annee:
            return True
        elif self.annee > d.annee:
            return False
        else:
            if self.mois < d.mois:
                return True
            elif self.mois > d.mois:
                return False
            else:
                if self.jour < d.jour:
                    return True
                elif self.jour > d.jour:
                    return False
                else:
                    return False
        



d1=Date()
d2=Date(20,7,1969)
print(d1,d2)
print(d1<d2, d2<d1, d1<d1)
