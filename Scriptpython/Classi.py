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

    #definisco <, serve per ordinare nel seguente modo sennò vari problemi con estrazione di stazioni 
    def __lt__(self,other):
        return (self.cStaz+self.cStato+self.cContea) <  (other.cStaz+other.cStato+other.cContea) 
    
    def __gt__(self,other):
        return self.data > other.data



    
    
class stazione():

    #classe che definisce una stazione singola con rilevazioni

    def __init__(self):
        self.nril = 0
        self.arrRil = np.empty(0)
        self.cStato = 0
        self.data = np.empty(0)
        self.mean = np.empty(0)

    #Utile per capire come analizzare le varie stazioni,visto che so quante stazioni ha ogni stato vedendo i dati
    
    def __lt__(self,other):
        return self.cStato < other.cStato

    

    def addril(self,r):
        self.arrRil = np.append(self.arrRil,r)
        self.nril = self.arrRil.size
        cStato=int(r.cStato)
        self.cStato = cStato
        #ogni volta che metti un ril vuoi mettere una data e una media corrispondenti 
        '''
        data=r.data
        self.data = data
        mean=r.mean
        self.mean = mean
        '''



class stato():
    #classe che definisce uno Stato con stazioni
    def __init__(self):
        self.nStaz = 0
        self.arrStaz = np.empty(0)
        

    #Utile per capire come analizzare le varie stazioni,visto che so quante stazioni ha ogni stato vedendo i dati
    
    def __lt__(self,other):
        return self.cStato < other.cStato

    
    
    def addStaz(self,s):
        self.arrStaz = np.append(self.arrStaz,s)
        self.nStaz = self.arrStaz.size
         
        
