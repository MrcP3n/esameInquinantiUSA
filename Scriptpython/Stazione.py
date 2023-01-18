import sys
import numpy as np

class rilevazione:

    #classe che definisce rilevazione
    
    def __init__(self,cStato,cContea,cStaz,data,mean):
        self.cStato=cStato
        self.cContea=cContea
        self.cStaz=cStaz
        self.data=data
        self.mean=mean

    def  __eq__(self,other):
        return self.data==other.data

    def __lt__(self,other):
        return self.cStaz < other.cStaz 
    
    def __gt__(self,other):
        return self.data > other.data

  #  def __ne__(self,other):
   #     return self.cStaz != other.cStaz


class stazione():

    #classe che definisce una stazione singola con rilevazioni

    def __init__(self):
        
        self.arrRil = np.empty(0)
        

        
    def addril(self,r):
        self.arrRil = np.append(self.arrRil,r)



#class Stato():

    #classe che definisce uno Stato con stazioni
        
