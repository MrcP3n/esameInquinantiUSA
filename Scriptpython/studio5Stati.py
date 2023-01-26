import numpy as np
import pandas as pd
import Stazione
import matplotlib.pyplot as plt
from scipy import constants , fft
import Funzioni as f



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
staz5Stati.sort(kind='mergesort')

print('Numero totale di stazioni: ', staz5Stati.size)  
for hh in staz5Stati[3].arrRil:
    print(hh.cStato, hh.cContea , hh.cStaz, hh.data ,hh.mean)
    

for i in range(35):
    print('-----Stazione{:}------'.format(i))
    print('nRilevazioni', staz5Stati[i].nril)


#estraggo array stazioni con funzione e andamenti temporali

stazCT2Date ,stazCT2Mean  = f.takeArr(staz5Stati[2])
stazCT3Date ,stazCT3Mean = f.takeArr(staz5Stati[3])
stazCT1Date ,stazCT1Mean = f.takeArr(staz5Stati[1])
title1='Confronto 2 stazioni Connecticut'

stazNY8Date , stazNY8Mean =f.takeArr(staz5Stati[8])
stazNY9Date , stazNY9Mean =f.takeArr(staz5Stati[9])
title2='Confronto 2 stazioni New York'

stazVA29Date , stazVA29Mean =f.takeArr(staz5Stati[29])
stazVA33Date , stazVA33Mean =f.takeArr(staz5Stati[33])
stazVA34Date , stazVA34Mean =f.takeArr(staz5Stati[34])
title3='Confronto 2 stazioni della Virginia '

stazPA13Date , stazPA13Mean =f.takeArr(staz5Stati[13])
stazPA15Date , stazPA15Mean =f.takeArr(staz5Stati[15])
title4='Confronto 2 stazioni Pennsylvania'

stazPA20Date , stazPA20Mean =f.takeArr(staz5Stati[20])
title5='Confronto stazione Pennsylvania con stazione New york'

stazPA24Date , stazPA24Mean =f.takeArr(staz5Stati[24])
stazVA31Date , stazVA31Mean =f.takeArr(staz5Stati[31])
title6='Confronto stazione Pennsylvania con stazione Virginia'

stazMD5Date , stazMD5Mean =f.takeArr(staz5Stati[5])
stazNY9Date , stazNY9Mean =f.takeArr(staz5Stati[9])
title7='Confronto stazione Maryland con stazione New york'
title8='Confronto 5 Stazioni degli stati contigui'
if False:
    f.graphInTime2(stazCT2Date ,stazCT2Mean,stazCT3Date ,stazCT3Mean,title1,'red')
    f.graphInTime2(stazNY8Date ,stazNY8Mean,stazNY9Date ,stazNY9Mean ,title2,'cyan')
    f.graphInTime2(stazVA29Date ,stazVA29Mean, stazVA33Date ,stazVA33Mean,title3,'orchid')
    f.graphInTime2(stazVA29Date ,stazVA29Mean, stazVA34Date ,stazVA34Mean,title3,'orchid')
    f.graphInTime2(stazPA13Date ,stazPA13Mean,stazPA15Date ,stazPA15Mean ,title4,'green')
    f.graphInTime2(stazPA20Date ,stazPA20Mean ,stazNY8Date ,stazNY8Mean ,title5,'darkviolet')
    f.graphInTime2(stazPA24Date ,stazPA24Mean ,stazVA31Date ,stazVA31Mean ,title6,'midnightblue')
    f.graphInTime2(stazMD5Date ,stazMD5Mean ,stazNY9Date ,stazNY9Mean ,title7,'limegreen')
    f.graphInTime5(stazCT1Date ,stazCT1Mean,stazMD5Date ,stazMD5Mean,stazNY9Date ,stazNY9Mean,stazPA20Date ,stazPA20Mean,stazVA31Date ,stazVA31Mean,title8)


#trasformata di fourier e freq 2 3 5 8 9 13 15 20 24 29 31 33 34
coffCT1 , cofFreqCT1 = f.trFour_freq(stazCT1Mean)
coffCT2 , cofFreqCT2 = f.trFour_freq(stazCT2Mean)
coffCT3 , cofFreqCT3 = f.trFour_freq(stazCT3Mean)
coffMD5 , cofFreqMD5 = f.trFour_freq(stazMD5Mean)
coffNY8 , cofFreqNY8 = f.trFour_freq(stazNY8Mean)
coffNY9 , cofFreqNY9 = f.trFour_freq(stazNY9Mean)
coffPA13 , cofFreqPA13 = f.trFour_freq(stazPA13Mean)
coffPA15 , cofFreqPA15 = f.trFour_freq(stazPA15Mean)
coffPA20 , cofFreqPA20 = f.trFour_freq(stazPA20Mean)
coffPA24 , cofFreqPA24 = f.trFour_freq(stazPA24Mean)
coffVA29 , cofFreqVA29 = f.trFour_freq(stazVA29Mean)
coffVA31 , cofFreqVA31 = f.trFour_freq(stazVA31Mean)
coffVA33 , cofFreqVA33 = f.trFour_freq(stazVA33Mean)
coffVA34 , cofFreqVA34 = f.trFour_freq(stazVA34Mean)


if True:
    title1='Spettro di potenza dei 5 stati contigui'
    f.graphSpettri5(coffCT1 , cofFreqCT1,coffMD5 , cofFreqMD5,coffNY9 , cofFreqNY9,coffPA20 , cofFreqPA20, coffVA31 , cofFreqVA31,title1)

'''
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

