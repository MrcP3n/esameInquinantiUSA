import numpy as np
import pandas as pd
import Classi
import matplotlib.pyplot as plt
from scipy import constants , fft
import Funzioni as f



p5stati='/home/marco-ubu/esameInquinantiUSA/DatiProgetto/dati5Stati.csv'

ril5Stati=f.getRilevaz5(p5stati)

ril5Stati.sort(kind='mergesort')
#print(ril5Stati)

for h in ril5Stati:
    print(h.cStato, h.cContea, h.cStaz, h.data, h.mean)
print('Numero totale di rilevazioni:', ril5Stati.size)

staz5Stati=f.getStazioni(ril5Stati)
staz5Stati.sort(kind='mergesort')

print('--------------------------------')
print('Numero totale di stazioni: ', staz5Stati.size)
for hh in staz5Stati[3].arrRil:
    print(hh.cStato, hh.cContea , hh.cStaz, hh.data ,hh.mean)
    

for i in range(35):
    print('-----Stazione{:}------'.format(i))
    print('nRilevazioni', staz5Stati[i].nril)
print('Numero totale di stazioni: ', staz5Stati.size)  


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
coffCT1 , cofFreqCT1 , maxCT1 = f.trFour_freq(stazCT1Mean)
coffCT2 , cofFreqCT2 , maxCT2 = f.trFour_freq(stazCT2Mean)
coffCT3 , cofFreqCT3 , maxCT3 = f.trFour_freq(stazCT3Mean)
coffMD5 , cofFreqMD5 , maxMD5 = f.trFour_freq(stazMD5Mean)
coffNY8 , cofFreqNY8 , maxNY8 = f.trFour_freq(stazNY8Mean)
coffNY9 , cofFreqNY9 , maxNY9 = f.trFour_freq(stazNY9Mean)
coffPA13 , cofFreqPA13 , maxPA13 = f.trFour_freq(stazPA13Mean)
coffPA15 , cofFreqPA15 , maxPA15 = f.trFour_freq(stazPA15Mean)
coffPA20 , cofFreqPA20 , maxPA20 = f.trFour_freq(stazPA20Mean)
coffPA24 , cofFreqPA24 , maxPA24 = f.trFour_freq(stazPA24Mean)
coffVA29 , cofFreqVA29 , maxVA29 = f.trFour_freq(stazVA29Mean)
coffVA31 , cofFreqVA31 , maxVA31 = f.trFour_freq(stazVA31Mean)
coffVA33 , cofFreqVA33 , maxVA33 = f.trFour_freq(stazVA33Mean)
coffVA34 , cofFreqVA34 , maxVA34 = f.trFour_freq(stazVA34Mean)

modcofCT1 = np.absolute(coffCT1)**2
modcofMD5 = np.absolute(coffMD5)**2
modcofNY9 = np.absolute(coffNY9)**2
modcofPA20 = np.absolute(coffPA20)**2
modcofVA31 = np.absolute(coffVA31)**2

if False:
    print('Stazione CT: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofCT1[maxCT1], cofFreqCT1[maxCT1], 1/cofFreqCT1[maxCT1]))
    print('Stazione MD: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofMD5[maxMD5], cofFreqMD5[maxMD5], 1/cofFreqMD5[maxMD5]))
    print('Stazione NY: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofNY9[maxNY9], cofFreqNY9[maxNY9], 1/cofFreqNY9[maxNY9]))
    print('Stazione PA: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofPA20[maxPA20], cofFreqPA20[maxPA20], 1/cofFreqPA20[maxPA20]))
    print('Stazione VA: Massimo : {:f} - Freq {:f} - Periodo: {:f}'.format(modcofVA31[maxVA31], cofFreqVA31[maxVA31], 1/cofFreqVA31[maxVA31]))

if False:
    title='Spettro di potenza dei 5 stati contigui in funzione della frequenza'
    f.graphSpettri5(coffCT1 , cofFreqCT1,coffMD5 , cofFreqMD5,coffNY9 , cofFreqNY9,coffPA20 , cofFreqPA20, coffVA31 , cofFreqVA31,title)
    title='Spettro di potenza dei 5 stati contigui in funzione del periodo'
    f.graphSpettri5Per(coffCT1 , cofFreqCT1,coffMD5 , cofFreqMD5,coffNY9 , cofFreqNY9,coffPA20 , cofFreqPA20, coffVA31 , cofFreqVA31,title)
    
'''Correlazione con coeff'''    


'''Filtri'''
cofFilCT1=f.trInv(coffCT1,1e5,stazCT1Mean)
cofFilCT2=f.trInv(coffCT2,1e5,stazCT2Mean)
cofFilCT3=f.trInv(coffCT3,1e5,stazCT3Mean)
cofFilNY8=f.trInv(coffNY8,1e6,stazNY8Mean)
cofFilNY9=f.trInv(coffNY9,1e6,stazNY9Mean)
cofFilPA13=f.trInv(coffPA13,2e6,stazPA13Mean)
cofFilPA15=f.trInv(coffPA15,2e6,stazPA15Mean)
cofFilPA20=f.trInv(coffPA20,2e6,stazPA20Mean)
cofFilPA24=f.trInv(coffPA24,2e6,stazPA24Mean)#togli una di PA
cofFilVA29=f.trInv(coffVA29,5e7,stazVA29Mean)#togli una di VA
cofFilVA31=f.trInv(coffVA31,5e7,stazVA31Mean)
cofFilVA33=f.trInv(coffVA33,5e7,stazVA33Mean)
cofFilVA34=f.trInv(coffVA34,5e7,stazVA34Mean)
cofFilMD5=f.trInv(coffMD5,2e6,stazMD5Mean)

'''Dati originali rispetto a filtrati'''



'''Rumori'''
if True:
    title='Grafico andamento della differenza tra dati originali e filtrati delle stazioni CT1 CT2 CT3 e NY8'
    f.graphRumori(stazCT1Date,coffCT1,cofFilCT1,stazCT2Date,coffCT2,cofFilCT2,stazCT3Date,coffCT3,cofFilCT3,stazNY8Date,coffNY8,cofFilNY8,title)
    title='Grafico andamento della differenza tra dati originali e filtrati delle stazioni  NY9 PA13,PA15 e PA24'
    f.graphRumori(stazCT1Date,coffCT1,cofFilCT1,stazCT2Date,coffCT2,cofFilCT2,stazCT3Date,coffCT3,cofFilCT3,stazNY8Date,coffNY8,cofFilNY8,title)
    title='Grafico andamento della differenza tra dati originali e filtrati delle stazioni VA29,VA31,VA34 e MD5'
    f.graphRumori(stazCT1Date,coffCT1,cofFilCT1,stazCT2Date,coffCT2,cofFilCT2,stazCT3Date,coffCT3,cofFilCT3,stazNY8Date,coffNY8,cofFilNY8,title)
    
    '''
    print(len(stazCT1Date),len(coffCT1),len(cofFilCT1))
    '''

