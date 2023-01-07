import numpy as np


class Stazione:

    #classe che definisce stazione
    
    def __init__(self,cStato,cContea,cStaz,data,mean):
        self.cStato=cStato
        self.cContea=cContea
        self.cStaz=cStaz
        self.data=data
        self.mean=mean

    def  __eq__(self,other):
        return self.cStaz==other.cStaz

    def __lt(self,other):
        return self.cStaz < other.cStaz
    

    def __gt__(self,other):
        return self.cStaz > other.cStaz

    def __ne__(self,other):
        return self.cStaz != other.cStaz



    
