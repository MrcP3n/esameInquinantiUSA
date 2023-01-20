import numpy as np
import pandas as pd
import Stazione
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy import constants , fft
from scipy import stats



p5stati='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/dati5Stati.csv'

def getRilevaz(path):

    #Funzione legge file e restituisce array di stazioni
    df=pd.read_csv(path)
    
    staz = np.array([Stazione.rilevazione( r['c5Stati'], r['cContea5'], r['nSit5'],r['date5Stati'],r['O3mean5Stati'] ) for i, r in df.iterrows() ])

    return staz



ril5Stati=getRilevaz(p5stati)



ril5Stati.sort(kind='mergesort')
#print(ril5Stati)

    
for h in ril5Stati:
    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)
print('Numero totale di rilevazioni:', ril5Stati.size)



def getStazioni(arRil):
  '''  
    Funzione che crea un array di Stazione.stazioni a partire da un array ordinato di Stazione.rilevaz (arrRil)
    
    Due rilevazioni in stesso luogo, ril1 e ril2, sono raggruppati nella stessa stazione se:
       ril1.cStaz!=ril2.cStaz
inoltre per evitare che rilevazione con lo stesso codice di stazione ma presa in luoghi differenti finiscano insieme a causa della ripetizioni di questi codici in luoghi differenti si aggiunge la seguente condizione:
       codeTest!=codePrecStatoContea
  che controlla che le due rilevazioni abbiano la somma tra codice di contea e stato diversi  
   '''

  stazioni = np.empty(0)
  codePrecStaz = arRil[0].cStaz
  codePrecStatoContea = arRil[0].cStato+ arRil[0].cContea
  stazioni=np.append(stazioni,Stazione.stazione())
  for h in arRil:
      codeTest=h.cContea+h.cStato
      if (h.cStaz != codePrecStaz ) :
          stazioni = np.append( stazioni, Stazione.stazione() )
      elif(codeTest!=codePrecStatoContea):
          stazioni = np.append( stazioni, Stazione.stazione() )
          
      codePrecStatoContea = codeTest    
      codePrecStaz = h.cStaz   
      stazioni[-1].addril(h)    
  return stazioni




staz5Stati=getStazioni(ril5Stati)
print('Numero totale di stazioni: ', staz5Stati.size)  
#print(staz5Stati)
for hh in staz5Stati[0].arrRil:
    print(hh.cStato, hh.cContea , hh.cStaz, hh.data ,hh.mean ,staz5Stati[0])


'''
#trasformata di fourier e freq

cofft=fft.fft(armean)
sNyqu=0.5
cofFreq=sNyqu*fft.fftfreq(len(cofft),d=1)

#grafico spettro in funz freq

plt.plot(cofFreq[:int(cofft.size/2)],np.absolute(cofft[:int(cofft.size/2)])**2,'o', markersize=3)
plt.xscale('log')
plt.yscale('log')
plt.show()

#grafico spettro in funz di periodo

plt.plot(1/cofFreq[:int(cofft.size/2)],np.absolute(cofft[0:int(cofft.size/2)])**2,'o' ,markersize=3)
plt.xscale('log')
plt.yscale('log')
plt.show()
'''

#trasformo string in int
#d=dateNY[0]
#s=int(d[3])
#print(d,s,s+100)


